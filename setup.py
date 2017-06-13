#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import distribute_setup

    distribute_setup.use_setuptools()
except:
    pass

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import os
import re

with open('requirements.txt', 'r') as f:
    requires = [x.strip() for x in f if x.strip()]

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='monflux',
    author="peablog",
    author_email="peablog@qq.com",
    version='0.0.5',
    description="collecting and reporting redis/mysql/nginx metrics , save data to influxdb",
    long_description=readme,
    url='https://github.com/peablog/monflux',
    license='MIT License',
    packages=find_packages(exclude=['tests']),
    test_suite='tests',
    tests_require=requires,
    install_requires=requires,
    extras_require={'test': requires},
    classifiers = [],
)
