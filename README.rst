::

    usage: rdio [--version] [-v] [--log-file LOG_FILE] [-q] [-h] [--debug]

    Command line access to the Rdio API

    optional arguments:
      --version            show program's version number and exit
      -v, --verbose        Increase verbosity of output. Can be repeated.
      --log-file LOG_FILE  Specify a file to log output. Disabled by default.
      -q, --quiet          suppress output except warnings and errors
      -h, --help           show this help message and exit
                   show tracebacks on errors

    Commands:
      call           Make an OAuth 2.0 API call
      grant client   OAuth 2.0 Client Credentials grant
      grant code     OAuth 2.0 Authorization Code grant
      grant implicit  OAuth 2.0 Implicit grant
      grant user     OAuth 2.0 Resource Owner Credential grant
      help           print detailed help for another command


OAuth 1.0a
==========

Bellow are examples for the OAuth 1.0a 3-legged authentication method:

::

    $ rdio oauth1 auth -k <client key> -s <client secret>

Bellow is an example of using the Rdio ``get`` API method:

::

    $ rdio oauth1 call -k <client key> -s <client secret> -e <access secret> \
        -c <access secret> get 'keys=r139688'

To skip entering API keys, you can define the following environment variables:

::

  RDIO_OAUTH1_CLIENT_KEY
  RDIO_OAUTH1_CLIENT_SECRET
  RDIO_OAUTH1_ACCESS_TOKEN
  RDIO_OAUTH1_ACCESS_SECRET



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

  RDIO_OAUTH2_CLIENT_KEY
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
