# Shared media management settings

The majority of our apps use similar media settings, so we've shared that
common pattern here:

  - hosted on server
    - static files collected into `staticfiles/`
    - static files served by [whitenoise](http://whitenoise.evans.io/en/latest/)
    - uploaded media stored on s3 using [django-s3-folder-storage](https://github.com/jamstooks/django-s3-folder-storage)
  - running locally
    - static files served in debug mode or collected into `staticfiles` and served by whitenoise
    - medial files uploaded to a directory based on the `MEDIA_ROOT` environment variable

## Example

    # Media Settings
    from integration_settings.media.s3 import *
    INSTALLED_APPS += ('s3_folder_storage',)

    # you still have to tell it where you keep your static files in the project
    STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__), 'static'),)

## Environment Variables

`USE_S3` - if set at all, s3 will be used for uploaded media. if unset, media will be stored and served locally using `MEDIA_ROOT` env var.
`AWS_ACCESS_KEY_ID`
`AWS_SECRET_ACCESS_KEY`
`AWS_STORAGE_BUCKET_NAME`
`DEFAULT_S3_PATH` (optional, defaults to 'uploads')

**Optional**
`STATIC_ROOT` - this defaults to 'staticfiles', which should work for most use cases,
but you could override it with an environment variable or set it in your settings
below the import.

## WSGI configuration

You will need to modify your wsgi.py script to the following:

    from django.core.wsgi import get_wsgi_application
    from whitenoise.django import DjangoWhiteNoise

    application = get_wsgi_application()
    application = DjangoWhiteNoise(application)

## Local development

From time to time you may need to test media uploads locally and won't want to
connect to s3. For this, we often use an environment variable, like `USE_S3`.
Simply unset that variable and you're golden.

## Using a CDN

Quickly set the hosts with these environment variables:
 
`CDN_MEDIA_HOST` and `CDN_STATIC_HOST`

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
