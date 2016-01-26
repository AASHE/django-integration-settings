# Shared Logging Configuration Settings

This provides a shared settings file for consistent logging across AASHE
django applications.

## Example

    # include the shared aashe settings
    from integration_settings.logging.sentry import *
    # update INSTALLED_APPS
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)

'raven.contrib.django.raven_compat' is automatically added to INSTALLED_APPS.

## What it does

  - GetSentry integration for log tracking and event notifications
  - Logs to standard output for easy on-server log management

## Requirements

You'll need to install `raven` - add it to requirements.txt

### Environment variables

  - `RAVEN_DSN`
  - `LOGGING_LEVEL` (default is 'INFO')
