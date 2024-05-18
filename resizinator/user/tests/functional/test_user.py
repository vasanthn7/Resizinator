import pytest

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
class TestUserViewSet(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')

    def test_user_register(self):
        assert User.objects.count() == 1
        url = '/user/register/'
        data = {'username': 'test2', 'password': 'test2'}
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert User.objects.count() == 2
        assert response.data['detail'] == 'User created'

    def test_user_login(self):
        assert Token.objects.count() == 0
        url = '/user/login/'
        data = {'username': 'test', 'password': 'test'}
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert 'token' in response.data
        assert Token.objects.filter(key=response.data['token']).exists()

    # def test_get_image(self):
    #     url = f'/image/{self.image.id}/'
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     assert response.data['id'] == self.image.id
    #     assert response.data['original'] == 'http://testserver/test.jpg'

    # def test_post_image(self):
    #     url = '/image/'
    #     data = {'original': self.temporary_image()}
    #     response = self.client.post(url, data=data, format='multipart')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     assert response.data['original'] == 'http://testserver/images/test.jpg'

    #     # Clean up
    #     image = Image.objects.get(id=response.data['id'])
    #     image.delete()

    # def test_delete_image(self):
    #     url = f'/image/{self.image.id}/'
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     assert Image.objects.count() == 0
