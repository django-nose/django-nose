#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""django-nose packaging."""
import os
from codecs import open
from setuptools import setup, find_packages


def get_long_description(title):
    """Create the long_description from other files."""
    ROOT = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(ROOT, "README.rst"), "r", "utf8") as f:
        readme = f.read()
    body_tag = ".. Omit badges from docs"
    readme_body_start = readme.index(body_tag)
    assert readme_body_start
    readme_body = readme[readme_body_start + len(body_tag):]

    with open(os.path.join(ROOT, "changelog.rst"), "r", "utf8") as f:
        changelog = f.read()
    old_tag = ".. Omit older changes from package"
    changelog_body_end = changelog.index(old_tag)
    assert changelog_body_end
    changelog_body = changelog[:changelog_body_end]

    bars = "=" * len(title)
    long_description = (
        """
%(bars)s
%(title)s
%(bars)s
%(readme_body)s

%(changelog_body)s

_(Older changes can be found in the full documentation)._
"""
        % locals()
    )
    return long_description


setup(
    name="django-nose",
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    description="Makes your Django tests simple and snappy",
    long_description=get_long_description("django-nose"),
    long_description_content_type="text/x-rst",  # Specify the content type
    author="Jeff Balogh",
    author_email="me@jeffbalogh.org",
    maintainer="John Whitlock",
    maintainer_email="jwhitlock@mozilla.com",
    url="http://github.com/jazzband/django-nose",
    license="BSD",
    packages=find_packages(exclude=["testapp", "testapp/*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "nose>=1.3.7",  # Updated to a more recent version of nose
        "Django>=1.8,<3.0"  # Specify Django compatibility
    ],
    test_suite="testapp.runtests.runtests",
    keywords="django nose django-nose",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Testing",
    ],
)
