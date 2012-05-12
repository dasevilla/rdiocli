import logging

from cliff.lister import Lister


class PlaylistLister(Lister):
    """Returns a user's playlists"""

    log = logging.getLogger(__name__)

    PLAYLIST_TYPE = None

    def get_parser(self, prog_name):
        parser = super(PlaylistLister, self).get_parser(prog_name)
        parser.add_argument('--user', help='key for a user', required=False)
        return parser

    def get_data(self, parsed_args):

        params = {}
        if parsed_args.user is not None:
            params['user'] = parsed_args.user

        result = self.app.call_rdio('getPlaylists', params)
        titles = result['result'][self.PLAYLIST_TYPE][0].keys()
        values = (n.values() for n in result['result'][self.PLAYLIST_TYPE])

        return (titles, values)


class OwnedPlaylistLister(PlaylistLister):
    """Fetch playlists the user owns"""
    PLAYLIST_TYPE = 'owned'


class CollabPlaylistLister(PlaylistLister):
    """Fetch playlists the user is collaborating with"""
    PLAYLIST_TYPE = 'collab'


class SubscribedPlaylistLister(PlaylistLister):
    """Fetch playlists the user is subscribed to"""
    PLAYLIST_TYPE = 'subscribed'
