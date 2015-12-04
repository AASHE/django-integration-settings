"""
    AASHE's shared media config
"""
import os

USE_S3 = os.environ.get('USE_S3', None)

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', 'staticfiles')

if USE_S3:
    INSTALLED_APPS += ('s3_folder_storage',)

    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", None)
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", None)

    # User uploaded media
    DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
    DEFAULT_S3_PATH = os.environ.get("DEFAULT_S3_PATH", 'uploads')
    MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
    MEDIA_URL = '//s3.amazonaws.com/%s/%s/' % (
        AWS_STORAGE_BUCKET_NAME, DEFAULT_S3_PATH)

    # Static files, served with whitenoise
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

else:
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.environ.get("MEDIA_ROOT", None)
