#!/usr/bin/env python
# from distutils.core import setup
from setuptools import setup

setup(
    name='prerender-health-checks',
    version='0.1',
    description='prerender health checks',
    url='https://github.com/bognix/prerender-health-checks',
    author='Bogna "bognix" Knychala',
    install_requires=['pytest==2.8.7', 'requests==2.0.1',
                      'virtualenv==1.11.6', 'nose==1.3.0'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    author_email='bogna.ka@gmail.com',
    packages=['tests'],
    include_package_data=True
)
