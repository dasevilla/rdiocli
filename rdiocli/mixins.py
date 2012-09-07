from cliff.lister import Lister
from cliff.show import ShowOne


class RdioLister(Lister):
    def get_parser(self, prog_name):
        parser = super(RdioLister, self).get_parser(prog_name)
        parser.add_argument('--extras', help='extra arguments', required=False)
        return parser

    def rdio_params(self, parsed_args, params=None):
        if params is None:
            params = {}

        if parsed_args.extras:
            params['extras'] = parsed_args.extras

        return params


class RdioShowOne(ShowOne):
    def get_parser(self, prog_name):
        parser = super(RdioShowOne, self).get_parser(prog_name)
        parser.add_argument('--extras', help='extra arguments', required=False)
        return parser

    def rdio_params(self, parsed_args, params=None):
        if params is None:
            params = {}

        if parsed_args.extras:
            params['extras'] = parsed_args.extras

        return params
