#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='django-latch',
    version='0.1',
    description='Django latch module.',
    long_description='Django module for integrating latch with django',
    author='Javier Olascoaga',
    author_email='jolascoaga@rootedcon.es',
    license='Apache License 2.0',
    url='https://github.com/rootedcon/django-latch',
    packages= [ 'latch'],
    install_requires=[
        "Django>=1.5",
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
