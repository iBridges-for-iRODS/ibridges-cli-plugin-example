"""Main plugin file to show info."""
from ibridges.cli.base import BaseCliCommand


class CliInfo(BaseCliCommand):
    """Subcommand to get information from the server."""

    names = ["info"]
    description = "List information about the server or user."
    examples = ["", "--user"]

    @classmethod
    def _mod_parser(cls, parser):
        parser.add_argument(
            "--user",
            help="Show the information about the user instead of the server.",
            action="store_true"
        )
        return parser

    @staticmethod
    def run_shell(session, parser, args):
        """Give info to the user."""
        if args.user:
            print(f"{'User': <20}: {session.irods_session.username}")
            print(f"{'Home': <20}: {session.home}")
            print(f"{'Current collection': <20}: {session.cwd}")
        else:
            print(f"{'Host': <10}: {session.irods_session.host}")
            print(f"{'Port': <10}: {session.irods_session.port}")
            print(f"{'Version': <10}: {'.'.join(str(x) for x in session.server_version)}")

        # parser can be used to show errors with parser.error
