import pytest

from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from image.models import Image
from image.views import ImageViewSet


@pytest.mark.django_db
class TestImageViewSet(TestCase):

    def setUp(self):
        self.image = Image.objects.create(original='test.jpg')

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
        data = {'original': 'test.jpg'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert response.data['original'] == 'http://testserver/test.jpg'
