# -*- coding: utf-8 -*-
"""
isobmff
version: 0.1
"""

import sys
from setuptools import setup, find_packages

VERSION = '0.1'
REQUIRES = []

setup(
    name='isobmff',
    version=VERSION,
    description='The isobmff is a python library for '
                'reading/writing ISO base media file format.',
    license='MIT',
    author_email='minoruhiki@gmail.com',
    url='https://github.com/m-hiki/isobmff',
    keywords=["isobmff", "mp4"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)