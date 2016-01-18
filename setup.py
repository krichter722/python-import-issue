#!/usr/bin/python
# -*- coding: utf-8 -*- 

from setuptools import setup, find_packages

setup(
    name = "project",
    version="1.0",
    packages = find_packages(),
    entry_points={
        'console_scripts': [
            'project = project.project:main',
        ],
    },
)
