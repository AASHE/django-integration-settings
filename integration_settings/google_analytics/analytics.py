"""
    Configuration for adding Google Analytics to AASHE properties.
"""
import os

GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get(
    'GOOGLE_ANALYTICS_PROPERTY_ID', None)
