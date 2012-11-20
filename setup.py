#!/usr/bin/env python

PROJECT = 'rdio'

# Change docs/sphinx/conf.py too!
VERSION = '0.2'

# Bootstrap installation of Distribute
import distribute_setup
distribute_setup.use_setuptools()

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

    scripts=['distribute_setup.py'],

    provides=[],
    install_requires=['distribute', 'cliff', 'cliff-tablib', 'requests-oauth'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'rdio = rdiocli.main:main'
            ],
        'rdio.cli': [
            'oauth1_auth = rdiocli.oauth1.auth:OAuth1AuthCommand',
            'oauth1_call = rdiocli.oauth1.call:OAuth1Call',
            'oauth2_auth_code = rdiocli.oauth2.auth:AuthCodeGrant',
            'oauth2_auth_implicit = rdiocli.oauth2.auth:ImplicitGrant',
            'oauth2_auth_client = rdiocli.oauth2.auth:ClientGrant',
            'oauth2_auth_user = rdiocli.oauth2.auth:PasswordGrant',
            'oauth2_auth_refresh = rdiocli.oauth2.auth:RefreshGrant',
            'oauth2_call = rdiocli.oauth2.call:RdioCall',
            ],
        },

    zip_safe=False,
    )
