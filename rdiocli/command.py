import os

from cliff.command import Command


class RdioCommand(Command):
    API_URL = 'https://www.rdio.com/api/1/'

    def get_parser(self, prog_name):
        parser = super(RdioCommand, self).get_parser(prog_name)
        parser.add_argument('-u', '--url', help='rdio api endpoint',
            required=False, default=self.API_URL)
        parser.add_argument('-t', '--token', help='access token',
            required=False, default=os.getenv('RDIO_TOKEN'))
        parser.add_argument('-e', '--extras', help='extras arguments',
            required=False)
        return parser
