#!/usr/bin/env python
from setuptools import setup
import os


# Utility function to read README file
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-integration-settings',
    version='0.0.11',
    description="Reusable settings templates for tools we commonly integrate with.",
    author='AASHE',
    author_email='it@aashe.org',
    url='https://github.com/aashe/django-integration-settings',
    long_description=read("README.md"),
    packages=[
        'integration_settings',
        'integration_settings.logging',
        'integration_settings.media',
        'integration_settings.google_analytics',
        'integration_settings.authentication',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
    ],
    test_suite=None,
    install_requires=[],
    dependency_links=[]
)
