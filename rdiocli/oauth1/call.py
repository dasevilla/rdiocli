from __future__ import unicode_literals
import json
import os

from base import OAuth1Command, OAuthException
from requests_oauthlib import OAuth1
import requests


class OAuth1Call(OAuth1Command):
    """
    Base class for all Rdio OAuth 1.0a API call requests
    """

    API_URL = 'http://api.rdio.com/1/'

    def get_description(self):
        return "Make an OAuth 1.0a API call"

    def get_parser(self, prog_name):
        parser = super(OAuth1Call, self).get_parser(prog_name)

        parser.add_argument('-e', '--access-token', help='OAuth 1.0a token',
            required=False, default=os.getenv('RDIO_OAUTH1_ACCESS_TOKEN'))
        parser.add_argument('-c', '--access-secret', help='OAuth 1.0a secret',
            required=False, default=os.getenv('RDIO_OAUTH1_ACCESS_SECRET'))
        parser.add_argument('-a', '--api-url',
            help='Rdio OAuth 1.0a authorization endpoint',
            required=False, default=self.API_URL)
        parser.add_argument('method', help='API method to call')
        parser.add_argument('param', help='API method parameter', nargs='*')

        return parser

    def take_action(self, parsed_args):
        oauth = OAuth1(parsed_args.client_token,
                       client_secret=parsed_args.client_secret,
                       resource_owner_key=parsed_args.access_token,
                       resource_owner_secret=parsed_args.access_secret)

        payload = {
            'method': parsed_args.method
        }

        for param in parsed_args.param:
            k, v = param.split('=')
            payload[k] = v

        r = requests.post(parsed_args.api_url, auth=oauth, data=payload)

        if r.status_code != 200:
            raise OAuthException('Bad response %s' % r.text)

        if r.json['status'] == 'error':
            raise OAuthException('Rdio API error: %s' % r.json['message'])

        print json.dumps(r.json, sort_keys=True, indent=2)
