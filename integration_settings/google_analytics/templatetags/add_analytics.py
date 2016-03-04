"""
    A template tag to load google analytics script within a django template.
    Returns GA script only if Debug=False.
"""
from django import template
import os

register = template.Library()


@register.inclusion_tag('analytics.html')
def add_analytics():
    return None


@register.assignment_tag
def toggle_analytics():
    toggle = os.environ.get('GOOGLE_ANALYTICS_PROPERTY_ID', None) and not os.environ.get('DEBUG', False)
    if not toggle:
        return False
    return True
