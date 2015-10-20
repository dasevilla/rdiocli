::

  usage: rdio [--version] [-v] [--log-file LOG_FILE] [-q] [-h] [--debug]

  Command line access to the Rdio API

  optional arguments:
    --version            show program's version number and exit
    -v, --verbose        Increase verbosity of output. Can be repeated.
    --log-file LOG_FILE  Specify a file to log output. Disabled by default.
    -q, --quiet          suppress output except warnings and errors
    -h, --help           show this help message and exit
    --debug              show tracebacks on errors

  Commands:
    help           print detailed help for another command
    oauth2 auth client  OAuth 2.0 Client Credentials grant
    oauth2 auth code  OAuth 2.0 Authorization Code grant
    oauth2 auth implicit  OAuth 2.0 Implicit grant
    oauth2 auth user  OAuth 2.0 Resource Owner Credential grant
    oauth2 call    Make an OAuth 2.0 API call


OAuth 2.0
=========

Bellow are examples for the OAuth 2.0 grant methods:

::

    $ rdio oauth2 grant code -k <client key> -s <client secret>
        -r <redirect uri>

    $ rdio oauth2 grant implicit -k <client key> -s <client secret>
        -r <redirect uri>

    $ rdio oauth2 grant user -k <client key> -s <client secret>
        -e test@example.com

    $ rdio oauth2 grant client -k <client key> -s <client secret>

Bellow is an example of using the Rdio ``get`` API method:

::

    $ rdio oauth2 call -t <client key> get 'keys=r139688'

To skip entering API keys, you can define the following environment variables:

::

  RDIO_OAUTH2_CLIENT_ID
  RDIO_OAUTH2_CLIENT_SECRET
  RDIO_OAUTH2_ACCESS_TOKEN


Developing
==========

::

    $ mkvirtualenv rdiocli
    $ git clone git://github.com/dasevilla/rdiocli.git rdiocli
    $ cd rdiocli
    $ pip install -r requirements.txt
    $ python setup.py develop
    $ tox # Test source using pep8, pyflakes
