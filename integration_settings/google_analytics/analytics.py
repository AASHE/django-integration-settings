"""
    Configuration for adding Google Analytics to AASHE properties.
"""

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-1056760-1'
GOOGLE_ANALYTICS_DOMAIN = 'aashe.org'

TEMPLATE_CONTEXT_PROCESSORS += (
    'integration_settings.google_analytics.context_processor.google_analytics',
)
