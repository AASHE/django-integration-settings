# Shared Logging Configuration Settings

This provides a shared settings file for consistent logging across AASHE
django applications.

## Example

    # include the shared aashe settings
    from integration_settings.logging.sentry import *
    # update INSTALLED_APPS
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)

## What it does

  - GetSentry integration for log tracking and event notifications
  - Logs to standard output for easy on-server log management

## Requirements

You'll need to install `raven` - add it to requirements.txt

### Environment variables

  - `RAVEN_DSN`
  - `LOGGING_LEVEL` (default is 'INFO')

# FlyData Integration Notes

FlyData provides a logging aggregation service, which is handy for
Heroku deployments since Heroku logs are a stream of ephemeral
entries, and if you don't catch them, they evaporate.

## How to set FlyData up

0. Add FlyData add-on to your app in the Heroku dashboard.  Start with
   the free option -- it's probably fat enough.

0. Create an S3 bucket to hold your app's logs. Name it "[heroku-app-name]-logs".

0. Click on the FlyData add-on in your Heroku dashboard to open the
   FlyData dashboard. Click on the Settings entry in the menu bar.

0. Enter the name of the S3 bucket you created. You can default all
   the other settings.

0. Go back to S3 and add list, upload/delete, and view permissions for
   "aws@flydata.co".

## How to access your FlyData logs

- You'll need to download your logs from S3 to view them.

- Log messages are split into three subdirectories, one for API, one
  for system, and one for your app. (You can read about the different
  type of Heroku log entries at
  [https://devcenter.heroku.com/articles/logging].

- To download some logs, click on FlyData in your Heroku
  dashboard. You'll see a "Download" link for each type of log.

- Click on one of those, and you'll get to specify a date range of
  entries to download. The logs will come down as a zipped tar file.

- That zipped tar file contains a bunch of gzipped logs, in a
  year/month/day directory stucture. It's a pain. Here's one way to
  read them all:

    <!-- Why can't I get ```bash ...``` to work for these lines? -->
    - `$ gzip -xzf <downloaded-filename>.tgz`
    - `$ cd <downloaded-filename>`
    - ``$ gzcat `find . -name "*.gz" -print` | less``
