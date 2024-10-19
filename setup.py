#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""django-nose packaging."""
import os
from codecs import open
from setuptools import setup, find_packages


def get_long_description(title):
    """Create the long_description from other files."""
    ROOT = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(ROOT, "README.rst"), "r", "utf-8") as readme_file:
        readme = readme_file.read()
    
    body_tag = ".. Omit badges from docs"
    readme_body_start = readme.find(body_tag)
    if readme_body_start == -1:
        raise ValueError(f"Body tag '{body_tag}' not found in README.")
    readme_body = readme[readme_body_start + len(body_tag):]

    with open(os.path.join(ROOT, "changelog.rst"), "r", "utf-8") as changelog_file:
        changelog = changelog_file.read()
    
    old_tag = ".. Omit older changes from package"
    changelog_body_end = changelog.find(old_tag)
    if changelog_body_end == -1:
        raise ValueError(f"Old tag '{old_tag}' not found in changelog.")
    changelog_body = changelog[:changelog_body_end]

    bars = "=" * len(title)
    long_description = (
        f"""
{bars}
{title}
{bars}
{readme_body}

{changelog_body}

_(Older changes can be found in the full documentation)._
"""
    )
    return long_description


setup(
    name="django-nose",
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    description="Makes your Django tests simple and snappy",
    long_description=get_long_description("django-nose"),
    author="Jeff Balogh",
    author_email="me@jeffbalogh.org",
    maintainer="John Whitlock",
    maintainer_email="jwhitlock@mozilla.com",
    url="http://github.com/jazzband/django-nose",
    license="BSD",
    packages=find_packages(exclude=["testapp", "testapp/*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=["nose>=1.2.1"],
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
