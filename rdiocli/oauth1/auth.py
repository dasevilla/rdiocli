import urlparse

from oauth_hook import OAuthHook
import requests

from base import OAuth1Command, OAuthException


class OAuth1AuthCommand(OAuth1Command):
    """
    Base class for all Rdio OAuth 1.0a authorization requests
    """

    REQUEST_TOKEN_URL = 'http://api.rdio.com/oauth/request_token'
    ACCESS_TOKEN_URL = 'http://api.rdio.com/oauth/access_token'
    AUTHORIZE_URL = 'https://www.rdio.com/oauth/authorize'

    def get_description(self):
        return "Request OAuth 1.0a access credentials"

    def get_parser(self, prog_name):
        parser = super(OAuth1AuthCommand, self).get_parser(prog_name)

        parser.add_argument('-r', '--request-token-url',
            help='Rdio OAuth 1.0a request token endpoint',
            required=False, default=self.REQUEST_TOKEN_URL)
        parser.add_argument('-a', '--access-token-url',
            help='Rdio OAuth 1.0a access token endpoint',
            required=False, default=self.ACCESS_TOKEN_URL)
        parser.add_argument('-u', '--authorization-url',
            help='Rdio OAuth 1.0a authorization endpoint',
            required=False, default=self.AUTHORIZE_URL)

        return parser

    def get_temporary_credentials(self, client_token, client_secret):
        oauth_hook = OAuthHook(
            header_auth=True,
            consumer_key=client_token,
            consumer_secret=client_secret,
        )

        hooks = {'pre_request': oauth_hook}
        payload = {
            'test': 1  # Hack so requests-oauth will send content-length
        }
        r = requests.post(self.REQUEST_TOKEN_URL, hooks=hooks, data=payload)

        if r.status_code != 200:
            raise OAuthException('Bad response %s' % r.text)

        qs = urlparse.parse_qs(r.text)
        temporary_token = qs['oauth_token'][0]
        temporary_secret = qs['oauth_token_secret'][0]

        return (temporary_token, temporary_secret)

    def get_access_credentials(self, client_token, client_secret,
        temporary_token, temporary_secret, oauth_verifier):

        oauth_hook = OAuthHook(
            header_auth=True,
            consumer_key=client_token,
            consumer_secret=client_secret,
            access_token=temporary_token,
            access_token_secret=temporary_secret,
        )

        hooks = {'pre_request': oauth_hook}
        payload = {
            'test': 1,  # Hack so requests-oauth will send content-length
            'oauth_verifier': oauth_verifier
        }
        r = requests.post(self.ACCESS_TOKEN_URL, hooks=hooks, data=payload)

        if r.status_code != 200:
            raise OAuthException('Bad response %s' % r.text)

        qs = urlparse.parse_qs(r.text)
        access_token = qs['oauth_token'][0]
        access_token_secret = qs['oauth_token_secret'][0]

        return (access_token, access_token_secret)

    def take_action(self, parsed_args):

        temporary_token, temporary_secret = self.get_temporary_credentials(
            parsed_args.client_token,
            parsed_args.client_secret
        )

        print 'Visit %s?oauth_callback=oob&oauth_token=%s' % (
            self.AUTHORIZE_URL, temporary_token)
        oauth_verifier = raw_input('Please enter your PIN:')

        access_token, access_token_secret = self.get_access_credentials(
            parsed_args.client_token,
            parsed_args.client_secret,
            temporary_token,
            temporary_secret,
            oauth_verifier,
        )

        print access_token, access_token_secret