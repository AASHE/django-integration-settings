# Shared media management settings

The majority of our apps use similar media settings, so we've shared that
common pattern here:

  - hosted on heroku
  - static files collected into `staticfiles`
  - static files served by [whitenoise](http://whitenoise.evans.io/en/latest/)
  - uploaded media stored on s3

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

### Signed vs. Unsigned AWS URLs

The URLs for your S3 served files can be signed or unsigned.

The advantage of a signed URL is that you can restrict access to it.
A disadvantage of a signed URL is that, by default, it includes an `Expires`
GET parameter that will prevent access to the resource after not much
time at all. Expired URLs return a 403 status code.

The advantage to an unsigned URL is that there is no restriction on
access -- anybody, any time, can load the resource.

If you want to serve unsigned AWS URLs, and you probably do, the environment
variable `AWS_QUERYSTRING_AUTH` must be set to False. That's done for you in
integration_settings.media.s3, so you don't have to change anything.

If you want to use signed AWS URLs, set `AWS_QUERYSTRING_AUTH` to True.

### Dependencies

- [whitenoise](http://whitenoise.evans.io/en/latest/)
- [django-s3-folder-storage](https://github.com/jamstooks/django-s3-folder-storage)

## Local development

From time to time you may need to test media uploads locally and won't want to
connect to s3. For this, we often use an environment variable, like `USE_S3`:

    # Media
    USE_S3 = os.environ.get('USE_S3', None)

    if USE_S3:
        INSTALLED_APPS += ('s3_folder_storage',)
        from integration_settings.media.s3 import *
    else:
        MEDIA_URL = "/media/"
        STATIC_URL = "/static/"
        MEDIA_ROOT = os.environ.get("MEDIA_ROOT", None)
        STATIC_ROOT = os.environ.get(
            "STATIC_ROOT", os.path.join(BASE_DIR, 'staticfiles'))

    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(__file__), 'static'),
    )

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

### CDN Support

CDN's are supported with two simple environment variables:

`CDN_MEDIA_HOST` and `CDN_STATIC_HOST`

For example, if you're using cloudfront, you might set `CDN_MEDIA_HOST` to:

    https://d21hv7tg6znr97.cloudfront.net
    
Check out the [whitenoise documentation](http://whitenoise.evans.io/en/latest/django.html#instructions-for-amazon-cloudfront)
for more information.

## Troubleshooting

"All my images disappeared!" Probably not, they're probably just 403. See the
'Signed vs. Unsigned AWS URLs' section above.
