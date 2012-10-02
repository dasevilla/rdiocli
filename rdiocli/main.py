import logging
import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class RdioApp(App):

    log = logging.getLogger(__name__)

    def __init__(self):
        super(RdioApp, self).__init__(
            description='Command line access to the Rdio API',
            version='0.1',
            command_manager=CommandManager('rdio.cli'),
            )


def main(argv=sys.argv[1:]):
    myapp = RdioApp()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
