# coding: utf-8
"""The django_nose module for running tests with Nose in Django."""

from pkg_resources import get_distribution, DistributionNotFound
from django_nose.runner import BasicNoseRunner, NoseTestSuiteRunner
from django_nose.testcases import FastFixtureTestCase

# Import classes
# No need for assert statements; if the imports fail, an ImportError will be raised.

try:
    __version__ = get_distribution("django-nose").version
except DistributionNotFound:
    # Package is not installed
    __version__ = None  # Set version to None if not found

# You can now use BasicNoseRunner, NoseTestSuiteRunner, and FastFixtureTestCase in your code.
