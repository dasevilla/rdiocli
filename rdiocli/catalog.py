import logging

from cliff.lister import Lister


class AlbumsForArtistLister(Lister):
    """Returns a user's playlists"""

    log = logging.getLogger(__name__)

    PLAYLIST_TYPE = None

    def get_parser(self, prog_name):
        parser = super(AlbumsForArtistLister, self).get_parser(prog_name)
        parser.add_argument('artist', help='key for an artist', nargs=1)
        return parser

    def take_action(self, parsed_args):

        params = {'artist': parsed_args.artist[0]}

        result = self.app.call_rdio('getAlbumsForArtist', params)
        titles = result['result'][0].keys()
        values = (n.values() for n in result['result'])

        return (titles, values)
