"""
AASHE's shared settings for aashe-auth authentication backend package
"""

import os

# Environment Variables
AASHE_AUTH_API_KEY = os.environ.get("AASHE_AUTH_API_KEY", None)
AASHE_AUTH_DOMAIN = os.environ.get("AASHE_AUTH_DOMAIN", None)
AASHE_AUTH_URI = os.environ.get("AASHE_AUTH_URI", None)
AASHE_AUTH_XMLRPC_HASH = os.environ.get("AASHE_AUTH_XMLRPC_HASH", None)

AASHE_DRUPAL_URI = os.environ.get('AASHE_DRUPAL_URI', None)
AASHE_DRUPAL_KEY = os.environ.get('AASHE_DRUPAL_KEY', None)
AASHE_DRUPAL_KEY_DOMAIN = os.environ.get('AASHE_DRUPAL_KEY_DOMAIN', None)
AASHE_DRUPAL_COOKIE_SESSION = os.environ.get(
    'AASHE_DRUPAL_COOKIE_SESSION', None)
AASHE_DRUPAL_COOKIE_DOMAIN = os.environ.get('AASHE_DRUPAL_COOKIE_DOMAIN', None)

#Authentication Backend
AUTHENTICATION_BACKENDS += 'aashe.aasheauth.backends.AASHEBackend'
