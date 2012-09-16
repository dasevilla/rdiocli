import os
import json
import getpass
import urllib
import sys

from cliff.command import Command
import requests
from requests.auth import HTTPBasicAuth


class AuthCommand(Command):
    TOKEN_URL = 'https://www.rdio.com/oauth2/token'
    AUTHORIZE_URL = 'https://www.rdio.com/oauth2/authorize'

    def get_parser(self, prog_name):
        parser = super(AuthCommand, self).get_parser(prog_name)

        parser.add_argument('-t', '--token-url',
            help='Rdio OAuth 2.0 token endpoint',
            required=False, default=self.TOKEN_URL)
        parser.add_argument('-a', '--authorization-url',
            help='Rdio OAuth 2.0 authorization endpoint',
            required=False, default=self.AUTHORIZE_URL)
        parser.add_argument('-k', '--key', help='OAuth 2.0 key',
            required=False, default=os.getenv('RDIO_CLIENT_KEY'))
        parser.add_argument('-s', '--secret', help='OAuth 2.0 secret',
            required=False, default=os.getenv('RDIO_CLIENT_SECRET'))
        parser.add_argument('-c', '--scope', help='OAuth 2.0 scope',
            required=False,)

        return parser

    def token_request(self, parsed_args, payload):
        r = requests.post(parsed_args.token_url,
            auth=HTTPBasicAuth(parsed_args.key, parsed_args.secret),
            data=payload)

        print json.dumps(r.json, sort_keys=True, indent=2)


class AuthCodeGrant(AuthCommand):

    def get_description(self):
        return "OAuth 2.0 Authorization Code grant"

    def get_parser(self, prog_name):
        parser = super(AuthCodeGrant, self).get_parser(prog_name)

        parser.add_argument('-r', '--redirect-uri',
            help='URI to redirect back to after authorization',
            required=False)
        parser.add_argument('-e', '--state',
            help='State to be returned back after authorization',
            required=False)

        return parser

    def take_action(self, parsed_args):
        query = {
            'response_type': 'code',
            'client_id': parsed_args.key,
        }

        if parsed_args.scope is not None:
            query['scope'] = parsed_args.scope

        if parsed_args.state is not None:
            query['state'] = parsed_args.state

        if parsed_args.redirect_uri is not None:
            query['redirect_uri'] = parsed_args.redirect_uri

        auth_url = '%s?%s' % (parsed_args.authorization_url,
            urllib.urlencode(query))

        print 'Visit the authorization URL:'
        print auth_url

        print 'Enter the auth code:'
        auth_code = sys.stdin.readline().rstrip()

        payload = {
            'grant_type': 'authorization_code',
            'code': auth_code,
            'redirect_uri': parsed_args.redirect_uri,
        }

        self.token_request(parsed_args, payload)


class ImplicitGrant(AuthCommand):

    def get_description(self):
        return "OAuth 2.0 Implicit grant"

    def get_parser(self, prog_name):
        parser = super(ImplicitGrant, self).get_parser(prog_name)

        parser.add_argument('-r', '--redirect-uri',
            help='URI to redirect back to after authorization',
            required=False)
        parser.add_argument('-e', '--state',
            help='State to be returned back after authorization',
            required=False)

        return parser

    def take_action(self, parsed_args):
        query = {
            'response_type': 'token',
            'client_id': parsed_args.key,
        }

        if parsed_args.scope is not None:
            query['scope'] = parsed_args.scope

        if parsed_args.state is not None:
            query['state'] = parsed_args.state

        if parsed_args.redirect_uri is not None:
            query['redirect_uri'] = parsed_args.redirect_uri

        auth_url = '%s?%s' % (parsed_args.authorization_url,
            urllib.urlencode(query))

        print 'Visit the authorization URL:'
        print auth_url


class PasswordGrant(AuthCommand):

    def get_description(self):
        return "OAuth 2.0 Resource Owner Credential grant"

    def get_parser(self, prog_name):
        parser = super(PasswordGrant, self).get_parser(prog_name)

        parser.add_argument('-e', '--email', help='Rdio email address')
        parser.add_argument('-p', '--password', help='Rdio password',
            required=False)

        return parser

    def take_action(self, parsed_args):
        if parsed_args.password is None:
            parsed_args.password = getpass.getpass()

        payload = {
            'grant_type': 'password',
            'username': parsed_args.email,
            'password': parsed_args.password,
        }

        if parsed_args.scope is not None:
            payload['scope'] = parsed_args.scope

        self.token_request(parsed_args, payload)


class ClientGrant(AuthCommand):

    def get_description(self):
        return "OAuth 2.0 Client Credentials grant"

    def take_action(self, parsed_args):
        payload = {
            'grant_type': 'client_credentials',
        }

        if parsed_args.scope is not None:
            payload['scope'] = parsed_args.scope

        self.token_request(parsed_args, payload)
