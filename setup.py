#!/usr/bin/env python

PROJECT = 'rdio'

# Change docs/sphinx/conf.py too!
VERSION = '0.2'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Command line access to the Rdio API',
    long_description=long_description,

    author='Devin Sevilla',
    author_email='dasevilla@gmail.com',

    url='https://github.com/dasevilla/rdiocli',
    download_url='https://github.com/dasevilla/rdiocli/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=[
        'cliff',
        'cliff-tablib',
        'requests',
        'requests-oauthlib'
    ],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'rdio = rdiocli.main:main'
            ],
        'rdio.cli': [
            'oauth2_auth_code = rdiocli.oauth2.auth:AuthCodeGrant',
            'oauth2_auth_implicit = rdiocli.oauth2.auth:ImplicitGrant',
            'oauth2_auth_client = rdiocli.oauth2.auth:ClientGrant',
            'oauth2_auth_user = rdiocli.oauth2.auth:PasswordGrant',
            'oauth2_auth_refresh = rdiocli.oauth2.auth:RefreshGrant',
            'oauth2_call = rdiocli.oauth2.call:RdioCall',
            'oembed = rdiocli.oembed.call:OEmbedCall',
            ],
        },

    zip_safe=False,
    )
