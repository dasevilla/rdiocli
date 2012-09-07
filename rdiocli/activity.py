import logging

from mixins import RdioLister


class HeavyRotationLister(RdioLister):
    """Returns a user's heavy rotation"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(HeavyRotationLister, self).get_parser(prog_name)
        parser.add_argument('--user', help='key for a user', required=False)
        parser.add_argument('--limit', help='number of results to return',
            required=False, type=int)
        parser.add_argument('--type', required=False,
            choices=('artists', 'albums'))
        return parser

    def take_action(self, parsed_args):

        params = {}
        if parsed_args.user is not None:
            params['user'] = parsed_args.user
        if parsed_args.limit is not None:
            params['limit'] = parsed_args.limit

        result = self.app.call_rdio('getHeavyRotation', params)

        titles = result['result'][0].keys()
        values = (n.values() for n in result['result'])

        return (titles, values)
