# Google Analytics Integration

This is a settings addition and template tag to enable Google Analytics
within your templates.

## Installation and Settings

    # Include the shared aashe settings
    from integration_settings.google_analytics import *
    # Update INSTALLED_APPS
    INSTALLED_APPS += ('integration_settings.google_analytics',)

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
