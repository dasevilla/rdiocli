import logging
import sys
import os
import json

from cliff.app import App
from cliff.commandmanager import CommandManager

import rdio


class RdioApp(App):

    log = logging.getLogger(__name__)

    def __init__(self):
        super(RdioApp, self).__init__(
            description='Command line access to the Rdio API',
            version='0.1',
            command_manager=CommandManager('rdio.cli'),
            )

    def initialize_app(self, argv):
        # Use the configuration that the rdio-python library uses
        config_path = os.path.expanduser('~/.rdio-tool.json')
        if os.path.exists(config_path):
            config = json.load(file(config_path))
        else:
            raise RuntimeError('missing ~/.rdio-tool.json')

        rdio_consumer = (str(config['consumer_key']),
            str(config['consumer_secret']))
        rdio_token = (str(config['auth_state']['access_token']['oauth_token']),
            str(config['auth_state']['access_token']['oauth_token_secret']))

        self.client = rdio.Rdio(rdio_consumer, rdio_token)

    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.log.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('got an error: %s', err)

    def call_rdio(self, method, params=dict()):
        result = self.client.call(method, params)

        if result['status'] == 'error':
            raise RuntimeError('Rdio API error: %s' % result['message'])
        return result


def main(argv=sys.argv[1:]):
    myapp = RdioApp()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
