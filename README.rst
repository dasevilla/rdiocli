::

    usage: rdio [--version] [-v] [-q] [-h] [--debug]

    Command line access to the Rdio API

    optional arguments:
        --version      show program's version number and exit
        -v, --verbose  Increase verbosity of output. Can be repeated.
        -q, --quiet    suppress output except warnings and errors
        -h, --help     show this help message and exit
        --debug        show tracebacks on errors

    Commands:
        collection artist albums  Returns a user's playlists
        collection artists  Returns a user's playlists
        get key        Fetch an object from Rdio using it's key
        get shortcode  Fetch an object from Rdio using it's short-code
        get url        Fetch an object from Rdio using it's URL
        help           print detailed help for another command
        playlist collab  Fetch playlists the user is collaborating with
        playlist owned  Fetch playlists the user owns
        playlist subscribed  Fetch playlists the user is subscribed to
        search         Search for objecs


Developing
==========

::

    $ mkvirtualenv rdiocli
    $ git clone git://github.com/dasevilla/rdiocli.git rdiocli
    $ cd rdiocli
    $ pip install -r requirements.txt
    $ python setup.py develop
    $ tox # Test source using pep8, pyflakes
