import logging

from cliff.show import ShowOne


class GetOneBase(ShowOne):
    "Base class for fetch an object from Rdio"

    ARGUMENT_NAME = None
    ARGUMENT_HELP = None
    RDIO_API_METHOD = None

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        if self.ARGUMENT_NAME is None:
            raise NotImplementedError('ARGUMENT_NAME is not defined')

        parser = super(GetOneBase, self).get_parser(prog_name)
        parser.add_argument(self.ARGUMENT_NAME, help=self.ARGUMENT_HELP)
        return parser

    def take_action(self, parsed_args):
        if self.RDIO_API_METHOD is None:
            raise NotImplementedError('RDIO_API_METHOD is not defined')

        params = self.get_rdio_params(parsed_args)
        result = self.app.call_rdio(self.RDIO_API_METHOD, params)
        payload = self.extract_data(parsed_args, result)

        return (payload.keys(), payload.values())

    def get_rdio_params(self, parsed_args):
        raise NotImplementedError('get_rdio_params method is not implemented')

    def extract_data(self, parsed_args, result):
        raise NotImplementedError('extract_data method is not implemented')


class GetOneByKey(GetOneBase):
    "Fetch an object from Rdio using it's key"

    ARGUMENT_NAME = 'key'
    ARGUMENT_HELP = 'An Rdio object key'
    RDIO_API_METHOD = 'get'

    def get_rdio_params(self, parsed_args):
        return {'keys': getattr(parsed_args, self.ARGUMENT_NAME)}

    def extract_data(self, parsed_args, result):
        return result['result'][getattr(parsed_args, self.ARGUMENT_NAME)]


class GetOneByShortCode(GetOneBase):
    "Fetch an object from Rdio using it's short-code"

    ARGUMENT_NAME = 'short_code'
    ARGUMENT_HELP = 'Everything after the http://rd.io/x'
    RDIO_API_METHOD = 'getObjectFromShortCode'

    def get_rdio_params(self, parsed_args):
        return {self.ARGUMENT_NAME: getattr(parsed_args, self.ARGUMENT_NAME)}

    def extract_data(self, parsed_args, result):
        return result['result']


class GetOneByUrl(GetOneBase):
    "Fetch an object from Rdio using it's URL"

    ARGUMENT_NAME = 'url'
    ARGUMENT_HELP = 'The path portion of the url'
    RDIO_API_METHOD = 'getObjectFromUrl'

    def get_rdio_params(self, parsed_args):
        return {self.ARGUMENT_NAME: getattr(parsed_args, self.ARGUMENT_NAME)}

    def extract_data(self, parsed_args, result):
        return result['result']
