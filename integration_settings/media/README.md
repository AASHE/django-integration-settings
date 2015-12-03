# Shared media management settings

The majority of our apps use similar media settings, so we've shared that
common pattern here.

## Example

    # include the shared aashe settings
    from integration_settings.media.s3 import *

    # Update INSTALLED_APPS
    INSTALLED_APPS += ('s3_folder_storage',)

    # tell it where you keep your static files in this app
    STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__), 'static'),)

## What it does

### Static Media

Static files can be hosted by the application server and served by
[whitenoise](http://whitenoise.evans.io/en/latest/). This configuration assumes
that the files will be collected into the "/staticfiles/" directory.

### Uploaded Media

Uploaded media is hosted on Amazon's S3 using [django-s3-folder-storage](https://github.com/jamstooks/django-s3-folder-storage).

## Requirements

You'll need to install `django-s3-folder-storage` - add it to requirements.txt

### Environment variables

You must define the following environment variables:

  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_STORAGE_BUCKET_NAME`
  - `DEFAULT_S3_PATH` (optional, defaults to 'uploads')

### WSGI configuration

You will need to modify your wsgi.py script to the following:

    from django.core.wsgi import get_wsgi_application
    from whitenoise.django import DjangoWhiteNoise

    application = get_wsgi_application()
    application = DjangoWhiteNoise(application)

### Dependencies

- [whitenoise](http://whitenoise.evans.io/en/latest/)
- [django-s3-folder-storage](https://github.com/jamstooks/django-s3-folder-storage)

## Local development

From time to time you may need to test media uploads locally and won't want to
connect to s3. For this, we often use an environment variable, like `USE_S3`:

    USE_S3 = os.environ.get('USE_S3', None)
    if USE_S3:
      from integration_settings.media.s3 import *
      INSTALLED_APPS += ('s3_folder_storage',)
      STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__), 'static'),)
    else:
      MEDIA_URL = "/media/"
      STATIC_URL = "/static/"
      MEDIA_ROOT = os.environ.get("MEDIA_ROOT", os.path.join(BASE_DIR, '/media/'))
      STATIC_ROOT = os.environ.get("STATIC_ROOT", os.path.join(BASE_DIR, '/static/'))

## Recommendations

You should set `MEDIA_ROOT` in your environment variables. I like to set up my
local directory structure this way:

    workspace/
      media/
        <project folders>
      src/
        <repos>

I keep my repos in src/ and create folders in media/ as necessary for projects
that store local uploaded media. This means I generally set my ENV var as
follows:

    MEDIA_ROOT = '/Users/jamstooks/aashe/workspace/media/<project>/'

This keeps media out of the repo and allows me to keep a consistent place for
media, even if I use a new branch.
