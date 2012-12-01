import json
import os

from cliff.command import Command
import requests

from base import OAuth2Exception
from bearer import BearerAuth


class RdioCall(Command):
    API_URL = 'https://www.rdio.com/api/1/'

    def get_description(self):
        return "Make an OAuth 2.0 API call"

    def get_parser(self, prog_name):
        parser = super(RdioCall, self).get_parser(prog_name)
        parser.add_argument('-u', '--url', help='Rdio API endpoint',
            required=False, default=self.API_URL)
        parser.add_argument('-t', '--token', help='access token',
            required=False, default=os.getenv('RDIO_OAUTH2_ACCESS_TOKEN'))
        parser.add_argument('-g', '--user-agent', help='User-Agent string',
            required=False)
        parser.add_argument('method', help='API method to call')
        parser.add_argument('param', help='API method parameter', nargs='*')
        return parser

    def take_action(self, parsed_args):
        headers = {}

        if parsed_args.user_agent:
            headers['User-Agent'] = parsed_args.user_agent

        payload = {
            'method': parsed_args.method
        }

        for param in parsed_args.param:
            k, v = param.split('=')
            payload[k] = v

        r = requests.post(parsed_args.url, auth=BearerAuth(parsed_args.token),
            data=payload, headers=headers)

        if r.status_code != 200:
            raise OAuth2Exception('Invalid HTTP response code: %s' %
                r.status_code)

        if r.json['status'] == 'error':
            raise OAuth2Exception('Rdio API error: %s' % r.json['message'])

        self.log_request(r)

        print json.dumps(r.json, sort_keys=True, indent=2)

    def log_request(self, r):
        self.app.log.debug('HTTP/1.1 %s %s', r.status_code, r.reason)
        self.log_headers(r.headers)
        self.app.log.debug('')  # Used to create a blank line

    def log_headers(self, header_dict):
        for k, v in sorted(header_dict.iteritems()):
            self.app.log.debug('%s: %s', k.title(), v)
