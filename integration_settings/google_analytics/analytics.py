"""
    Configuration for adding Google Analytics to AASHE properties.
"""
import os

GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get('GOOGLE_ANALYTICS_PROPERTY_ID', None)
GOOGLE_ANALYTICS_DOMAIN = os.environ.get('GOOGLE_ANALYTICS_DOMAIN', None)

TEMPLATE_CONTEXT_PROCESSORS += (
    'integration_settings.google_analytics.context_processor.google_analytics',
)
