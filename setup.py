#!/usr/bin/env python

PROJECT = 'rdio'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

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
    install_requires=['distribute', 'cliff', 'oauthlib'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'rdio = rdiocli.main:main'
            ],
        'rdio.cli': [
            'get_key = rdiocli.core:GetOneByKey',
            'get_shortcode = rdiocli.core:GetOneByShortCode',
            'get_url = rdiocli.core:GetOneByUrl',
            'search = rdiocli.search:SearchLister',
            'playlist_owned = rdiocli.playlist:OwnedPlaylistLister',
            'playlist_collab = rdiocli.playlist:CollabPlaylistLister',
            'playlist_subscribed = rdiocli.playlist:SubscribedPlaylistLister',
            'collection_artists = rdiocli.collection:ArtistsLister',
            ('collection_artist_albums ='
                ' rdiocli.collection:AlbumsForArtistLister'),
            ],
        },

    zip_safe=False,
    )
