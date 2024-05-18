from io import BytesIO

import boto3
from django.contrib.auth.models import User
from moto import mock_aws
import PIL.Image
import pytest
from unittest import mock

from image.models import Image
from image.tasks import resize_image


@pytest.fixture
def image():
    user = User.objects.create_user(username='test', password='test')
    return Image.objects.create(original='test.jpg', user=user)

@mock_aws
@pytest.mark.django_db
def test_resize_image(image):
    s3 = boto3.resource("s3", region_name="us-east-1")
    s3.create_bucket(Bucket='testbucket')

    assert image.small.name is None
    assert image.medium.name is None
    with mock.patch('image.tasks.default_storage') as mock_storage:
        mock_file = mock.MagicMock()
        temporary_image = PIL.Image.new('RGB', (100, 100), color='red')
        byte_io = BytesIO()
        temporary_image.save(byte_io, 'jpeg')
        byte_io.seek(0)
        mock_file.read.return_value = byte_io.read()
        mock_storage.open.return_value.__enter__.return_value = mock_file
        resize_image.apply(args=(image.id, )).get()

    image.refresh_from_db()
    assert image.small.name == 'small_test.jpg'
    assert image.medium.name == 'medium_test.jpg'
