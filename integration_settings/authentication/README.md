# Shared AASHE-Auth Settings

This provides a shared settings file for the use of the aashe-auth package.

## Installation and Settings

    pip install -e git+https://github.com/AASHE/aashe-auth.git@migrations#egg=aashe_auth

    # Include the shared aashe settings
    from integration_settings.authentication.aashe-auth import *
    # Update INSTALLED_APPS
    INSTALLED_APPS += ('aasheauth',)
    
Update MIDDLEWARE_CLASSES
    
    MIDDLEWARE_CLASSES = (
        ...
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'aashe.aasheauth.middleware.AASHEAccountMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        ...
    )    

## What it does

    - Enables aashe-auth authentication back-end for single sign-on with AASHE sites.

## Requirements

    - Django

## Environment variables

    - AASHE_AUTH_API_KEY  # aka SSO_API_KEY
    - AASHE_AUTH_DOMAIN  # aka STARS_DOMAIN
    - AASHE_AUTH_URI  # endpoint URI of AASHE XML-RPC service
    - (Optional) AASHE_AUTH_XMLRPC_HASH  # aka XMLRPC_USE_HASH, default True?
    - AASHE_DRUPAL_URI
    - AASHE_DRUPAL_KEY
    - AASHE_DRUPAL_KEY_DOMAIN
    - AASHE_DRUPAL_COOKIE_SESSION
    - AASHE_DRUPAL_COOKIE_DOMAIN

## Login and Logout Views

Update your URL configuration file:

     from aashe.aasheauth.views import LoginView, logout
     
     urlpatterns = [
         ...
         url(r'^login/', LoginView.as_view(), name='login'),
         url(r'^logout/', logout, name='logout'),
         ...
     ]
     
Include a Login link in your template. Construct the <a> tag such that it includes a "?next=" parameter like so:

     <a href="{% url "login" %}?next={{ request.path }}">
     
This will cause your session to redirect back to the page where the user clicked the Login link after a successful login.

The same is true for logging out:

    <a href="{% url "logout" %}?next={{ request.path }}">
