from io import BytesIO

import boto3
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from moto import mock_aws
import PIL.Image
import pytest
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch

from image.models import Image


@mock_aws
@pytest.mark.django_db
class TestImageViewSet(APITestCase):
    bucket_name = 'testbucket'

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.image = Image.objects.create(original='test.jpg', user=self.user)

        s3 = boto3.resource("s3", region_name="us-east-1")
        s3.create_bucket(Bucket=self.bucket_name)

    def temporary_image(self):
        bts = BytesIO()
        img = PIL.Image.new("RGB", (100, 100))
        img.save(bts, 'jpeg')
        return SimpleUploadedFile("test.jpg", bts.getvalue())

    def test_list_image(self):
        url = '/image/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert response .data['count'] == 1
        assert response.data['results'][0]['original'] == 'https://testbucket.s3.amazonaws.com/test.jpg'

    def test_get_image(self):
        url = f'/image/{self.image.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert response.data['id'] == self.image.id
        assert response.data['original'] == 'https://testbucket.s3.amazonaws.com/test.jpg'

    @patch('image.tasks.resize_image.delay')
    def test_create_image(self, mock_celery_task):
        url = '/image/'
        data = {'original': self.temporary_image()}
        response = self.client.post(url, data=data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        data = {'original': self.temporary_image()}
        response = self.client.post(url, data=data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert response.data['original'] == 'https://testbucket.s3.amazonaws.com/test.jpg'

        mock_celery_task.assert_called_once_with(response.data['id'])
        image = Image.objects.get(id=response.data['id'])
        image.delete()

    def test_delete_image(self):
        url = f'/image/{self.image.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        assert Image.objects.count() == 0
