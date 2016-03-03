# Google Analytics Integration

This is a settings addition and template tag to enable Google Analytics
within your templates.

## Installation and Settings

    # Update INSTALLED_APPS
    INSTALLED_APPS += ('integration_settings.google_analytics',)
    
    # Add env variables
    GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get('GOOGLE_ANALYTICS_PROPERTY_ID', None)
    GOOGLE_ANALYTICS_DOMAIN = os.environ.get('GOOGLE_ANALYTICS_DOMAIN', None)

    # Add context processor
    TEMPLATES['OPTIONS']['context_processors'] += (
        'integration_settings.google_analytics.context_processor.google_analytics',
    )

You can update each of these manually in your settings.py, or attempt:

    from integration_settings.google_analytics.analytics import *
    
Note: this sometimes raises the error that TEMPLATES is not defined.

## What it does

    Allows you to simply drop a single tag into your template to load
    Google Analytics.

## Requirements

    - Django

## Environment Variables

    GOOGLE_ANALYTICS_PROPERTY_ID
    GOOGLE_ANALYTICS_DOMAIN
    DEBUG

## Template Tag Usage

    Inside your base template for the project, insert....
    
        {% load google_analytics %}
        {% add_analytics %}
    
    No need for any conditionals, this is processed within the tag, which
    only returns the GA script if Debug = False.
