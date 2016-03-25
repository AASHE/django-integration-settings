"""
    AASHE's shared media config
"""
import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", None)

AWS_QUERYSTRING_AUTH = False  # Prefer unsigned S3 URLs.

# User uploaded media
DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = os.environ.get("DEFAULT_S3_PATH", 'uploads')
MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//s3.amazonaws.com/%s/%s/' % (
    AWS_STORAGE_BUCKET_NAME, DEFAULT_S3_PATH)

# Static files, served with whitenoise
STATIC_ROOT = 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# CDN Settings
STATIC_HOST = os.environ.get('CDN_STATIC_HOST', '')
STATIC_URL = STATIC_HOST + '/static/'

CDN_MEDIA_HOST = os.environ.get('CDN_MEDIA_HOST', None)
if CDN_MEDIA_HOST:
    MEDIA_URL = '//%s/%s/%s/' % (
        CDN_MEDIA_HOST, AWS_STORAGE_BUCKET_NAME, DEFAULT_S3_PATH)

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
