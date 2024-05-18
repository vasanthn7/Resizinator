from io import BytesIO

import pytest

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
import PIL.Image
from rest_framework import status

from image.models import Image


@pytest.mark.django_db
class TestImageViewSet(TestCase):

    def setUp(self):
        self.image = Image.objects.create(original='test.jpg')

    def temporary_image(self):
        bts = BytesIO()
        img = PIL.Image.new("RGB", (100, 100))
        img.save(bts, 'jpeg')
        return SimpleUploadedFile("test.jpg", bts.getvalue())

    def test_list_image(self):
        url = '/image/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert response .data['count'] == 1
        assert response.data['results'][0]['original'] == 'http://testserver/test.jpg'

    def test_get_image(self):
        url = f'/image/{self.image.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert response.data['id'] == self.image.id
        assert response.data['original'] == 'http://testserver/test.jpg'

    def test_post_image(self):
        url = '/image/'
        data = {'original': self.temporary_image()}
        response = self.client.post(url, data=data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert response.data['original'] == 'http://testserver/images/test.jpg'

        # Clean up
        image = Image.objects.get(id=response.data['id'])
        image.delete()

    def test_delete_image(self):
        url = f'/image/{self.image.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        assert Image.objects.count() == 0
