import logging

from mixins import RdioLister


class AlbumsForArtistLister(RdioLister):
    """Returns a user's playlists"""

    log = logging.getLogger(__name__)

    PLAYLIST_TYPE = None

    def get_parser(self, prog_name):
        parser = super(AlbumsForArtistLister, self).get_parser(prog_name)
        parser.add_argument('--user', help='key for a user', nargs='?')
        parser.add_argument('artist', help='key for an artist', nargs=1)
        return parser

    def take_action(self, parsed_args):

        params = self.rdio_params(parsed_args, {
            'artist': parsed_args.artist[0]
        })

        if parsed_args.user is not None:
            params['user'] = parsed_args.user

        result = self.app.call_rdio('getAlbumsForArtistInCollection', params)
        titles = result['result'][0].keys()
        values = (n.values() for n in result['result'])

        return (titles, values)


class ArtistsLister(RdioLister):
    """Returns a user's artists"""

    log = logging.getLogger(__name__)

    PLAYLIST_TYPE = None

    def get_parser(self, prog_name):
        parser = super(ArtistsLister, self).get_parser(prog_name)
        parser.add_argument('--user', help='key for a user', nargs='?')
        return parser

    def take_action(self, parsed_args):

        params = self.rdio_params(parsed_args)

        if parsed_args.user is not None:
            params['user'] = parsed_args.user

        result = self.app.call_rdio('getArtistsInCollection', params)
        titles = result['result'][0].keys()
        values = (n.values() for n in result['result'])

        return (titles, values)
