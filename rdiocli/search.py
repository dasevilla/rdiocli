import logging

from cliff.lister import Lister


class SearchLister(Lister):
    """Search for objecs"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(SearchLister, self).get_parser(prog_name)
        parser.add_argument('types', nargs=1,
            help='Comma separated list: Artist, Album, Track, Playlist, User')
        parser.add_argument('query', help='The search query', nargs=1)
        return parser

    def get_data(self, parsed_args):

        params = {'types': parsed_args.types[0], 'query': parsed_args.query[0]}

        result = self.app.call_rdio('search', params)
        titles = result['result']['results'][0].keys()

        values = []
        for n in result['result']['results']:
            n.update((k, None) for k in titles - n.viewkeys())
            values.append(n.values())

        return (titles, values)
