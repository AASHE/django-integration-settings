"""
    AASHE's shared logging config
"""
import os

INSTALLED_APPS += ('raven.contrib.django.raven_compat',)

RAVEN_CONFIG = {
    'dsn': os.environ.get('RAVEN_DSN', '/static/')
}
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'console': {
            'format': '%(asctime)s:%(levelname)s:%(name)s:%(message)s',
            'datefmt': '%m/%d/%Y-%H:%M:%S'
            },
        },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
            },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler'
            },
        },

    'loggers': {
        '': {
            'handlers': ['console', 'sentry'],
            'level': LOGGING_LEVEL,
            'propagate': False,
        },
    }
}

logging.config.dictConfig(LOGGING)
