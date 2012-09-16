import json

from command import RdioCommand


class RdioCall(RdioCommand):

    def get_description(self):
        return "Make an OAuth 2.0 API call"

    def get_parser(self, prog_name):
        parser = super(RdioCall, self).get_parser(prog_name)
        parser.add_argument('method', help='api method to call')
        parser.add_argument('param', help='api method parameter', nargs='*')
        return parser

    def take_action(self, parsed_args):
        result = self.app.api_call(parsed_args)
        print json.dumps(result, sort_keys=True, indent=2)
