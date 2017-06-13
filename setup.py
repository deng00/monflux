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

with open(os.path.join(os.path.dirname(__file__), 'monflux', '__init__.py')) as f:
    version = re.search("__version__ = '([^']+)'", f.read()).group(1)

with open('requirements.txt', 'r') as f:
    requires = [x.strip() for x in f if x.strip()]

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='monflux',
    author="peablog",
    author_email="peablog@qq.com",
    version=version,
    description="monflux redis/mysql or others app and save data to influxdb",
    long_description=readme,
    url='https://github.com/peablog/monflux',
    license='MIT License',
    packages=find_packages(exclude=['tests']),
    test_suite='tests',
    tests_require=requires,
    install_requires=requires,
    extras_require={'test': requires},
    classifiers=(
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    )
)
