# htaccess

Our dev sites should probably be password protected so that they aren't accidentally indexed by google or accessed by our users. This is pretty easy with [django-password-protect](https://github.com/plumdog/django-password-protect).

## Configuration

`pip install django-password-protect`

Add `'django_password_protect.PasswordProtectMiddleware'` to `MIDDLEWARE_CLASSES`

Update settings:

    PASSWORD_PROTECT = os.environ.get('PASSWORD_PROTECT', False)
    PASSWORD_PROTECT_USERNAME = os.environ.get('PASSWORD_PROTECT_USERNAME', None)
    PASSWORD_PROTECT_PASSWORD = os.environ.get('PASSWORD_PROTECT_PASSWORD', None)
    PASSWORD_PROTECT_REALM = os.environ.get('PASSWORD_PROTECT_REALM', 'Dev Site Auth')
  
Production sites won't have `PASSWORD_PROTECT` set, but other should set it to 1.
