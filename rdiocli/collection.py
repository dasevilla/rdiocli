import logging

from cliff.lister import Lister


class AlbumsForArtistLister(Lister):
    """Returns a user's playlists"""

    log = logging.getLogger(__name__)

    PLAYLIST_TYPE = None

    def get_parser(self, prog_name):
        parser = super(AlbumsForArtistLister, self).get_parser(prog_name)
        parser.add_argument('--user', help='key for a user', nargs='?')
        parser.add_argument('artist', help='key for an artist', nargs=1)
        return parser

    def get_data(self, parsed_args):

        params = {'artist': parsed_args.artist[0]}
        if parsed_args.user is not None:
            params['user'] = parsed_args.user

        result = self.app.call_rdio('getAlbumsForArtistInCollection', params)
        titles = result['result'][0].keys()
        values = (n.values() for n in result['result'])

        return (titles, values)


class ArtistsLister(Lister):
    """Returns a user's playlists"""

    log = logging.getLogger(__name__)

    PLAYLIST_TYPE = None

    def get_parser(self, prog_name):
        parser = super(ArtistsLister, self).get_parser(prog_name)
        parser.add_argument('--user', help='key for a user', nargs='?')
        return parser

    def get_data(self, parsed_args):

        params = {}
        if parsed_args.user is not None:
            params['user'] = parsed_args.user

        result = self.app.call_rdio('getArtistsInCollection', params)
        titles = result['result'][0].keys()
        values = (n.values() for n in result['result'])

        return (titles, values)
