"""
    A template tag to load google analytics script within a django template.
    Renders GA script if GOOGLE_ANALYTICS_PROPERTY_ID setting is not None
"""
from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('analytics.html')
def add_analytics():
    return {
        'GOOGLE_ANALYTICS_PROPERTY_ID': settings.GOOGLE_ANALYTICS_PROPERTY_ID}
