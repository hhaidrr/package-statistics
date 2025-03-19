from argparse import ArgumentParser

from package_statistics._constants import SUPPORTED_ARCHITECTURES

__all__ = ["initialize_parser"]


def initialize_parser(parser: ArgumentParser) -> None:
    """
    Initialize the command line argument parser with the required arguments.

    :param parser: The parse instance to initialize.
    """
    parser.add_argument(
        "architecture",
        type=str,
        choices=SUPPORTED_ARCHITECTURES,
        help="The architecture to download the Contents file for.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="The maximum number of packages to display in the output.",
        required=False,
        default=10,
    )
