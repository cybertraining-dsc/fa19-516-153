from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.cluster.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class ClusterCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_cluster(self, args, arguments):
        """
        ::

          Usage:
                cluster --file=FILE
                cluster list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        arguments.FILE = arguments['--file'] or None

        VERBOSE(arguments)

        m = Manager()

        if arguments.FILE:
            print("option a")
            m.list(path_expand(arguments.FILE))

        elif arguments.list:
            print("option b")
            m.list("just calling list without parameter")

        Console.error("This is just a sample")
        return ""
