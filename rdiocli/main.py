import logging
import os
import sys

import requests
from cliff.app import App
from cliff.commandmanager import CommandManager

from bearer import BearerAuth


class RdioApp(App):

    log = logging.getLogger(__name__)

    def __init__(self):
        super(RdioApp, self).__init__(
            description='Command line access to the Rdio API',
            version='0.1',
            command_manager=CommandManager('rdio.cli'),
            )

    def initialize_app(self, argv):
        auth_code = os.environ.get('RDIO_ACCESS_TOKEN')
        if auth_code is None:
            self.rdio_session = requests.session()
        else:
            self.rdio_session = requests.session(auth=BearerAuth(auth_code))

    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.log.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('got an error: %s', err)

    def call_rdio(self, method, params=dict()):
        api_url = 'https://www.rdio.com/api/1/'
        params['method'] = method
        result = self.rdio_session.post(api_url, data=params)

        if result.json['status'] == 'error':
            raise RuntimeError('Rdio API error: %s' % result.json['message'])
        return result.json

    def api_call(self, parsed_args):
        payload = {
            'method': parsed_args.method
        }

        for param in parsed_args.param:
            k, v = param.split('=')
            payload[k] = v

        if parsed_args.extras:
            payload['extras'] = parsed_args.extras

        print parsed_args.url, parsed_args.token, payload

        if parsed_args.token is None:
            result = self.rdio_session.post(parsed_args.url, data=payload)
        else:
            result = self.rdio_session.post(parsed_args.url, data=payload,
                auth=BearerAuth(parsed_args.token))

        if result.status_code != 200:
            raise RuntimeError('Invalid HTTP response code: %s' %
                result.status_code)

        if result.json['status'] == 'error':
            raise RuntimeError('Rdio API error: %s' % result.json['message'])
        return result.json


def main(argv=sys.argv[1:]):
    myapp = RdioApp()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
