import os

from cliff.command import Command


class OAuth1Command(Command):
    """
    Base class for all Rdio OAuth 1.0a requests
    """

    def get_parser(self, prog_name):
        parser = super(OAuth1Command, self).get_parser(prog_name)

        parser.add_argument('-k', '--client-token', help='OAuth 1.0a token',
            required=False, default=os.getenv('RDIO_OAUTH1_CLIENT_KEY'))
        parser.add_argument('-s', '--client-secret', help='OAuth 1.0a secret',
            required=False, default=os.getenv('RDIO_OAUTH1_CLIENT_SECRET'))

        return parser


class OAuthException(Exception):
    pass
