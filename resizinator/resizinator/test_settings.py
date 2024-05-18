from .settings import *

AWS_ACCESS_KEY_ID = 'testing'
AWS_SECRET_ACCESS_KEY = 'testing'
AWS_DEFAULT_REGION = 'us-east-1'
AWS_STORAGE_BUCKET_NAME = 'testbucket'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

DEFAULT_STORAGE = 'django.core.files.storage.FileSystemStorage'
