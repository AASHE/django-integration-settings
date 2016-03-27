# Google Analytics Integration

This is a settings addition and template tag to enable Google Analytics
within your templates.

## Installation and Settings

You'll need to set `GOOGLE_ANALYTICS_PROPERTY_ID`. You can do this either manually:

    GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get('GOOGLE_ANALYTICS_PROPERTY_ID', None)

Or you can include the setting helper and just set the environment variable:

    from integration_settings.google_analytics.analytics import *

## What it does

    Allows you to simply drop a single tag into your template to load Google Analytics.

## Template Tag Usage

Inside your base template for the project, insert....
    
    {% load google_analytics %}
    {% add_analytics %}
    
No need for any conditionals, this is processed within the tag, which
only renders the GA script if `GOOGLE_ANALYTICS_PROPERTY_ID` is set.

## Requirements

    - Django
