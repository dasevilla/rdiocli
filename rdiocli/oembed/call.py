import requests
from cliff.show import ShowOne


class OEmbedException(Exception):
    pass


class OEmbedCall(ShowOne):
    """
    Base class for all Rdio oEmbed requests
    """

    OEMBED_URL = 'https://www.rdio.com/api/oembed/'

    def get_description(self):
        return "Make an oEmbed call"

    def get_parser(self, prog_name):
        parser = super(OEmbedCall, self).get_parser(prog_name)

        parser.add_argument('url', help='Rdio URL')

        return parser

    def take_action(self, parsed_args):
        payload = {
            'format': 'json',
            'url': parsed_args.url,
        }
        r = requests.post(self.OEMBED_URL, params=payload)

        if r.status_code != 200:
            if r.status_code == 404:
                raise OEmbedException('Not Found')
            else:
                raise OEmbedException('Bad response %s' % r.text)

        r_payload = r.json()
        columns = r_payload.keys()
        data = r_payload.values()

        return (columns, data)
