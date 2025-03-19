from argparse import ArgumentParser, Namespace
from io import BytesIO
from package_statistics._arguments import initialize_parser
from package_statistics._constants import (
    CONTENT_FILE_NAME_TEMPLATE,
    DEBIAN_STABLE_REPOSITORY_URL,
    SUPPORTED_ARCHITECTURES,
)
import sys

from package_statistics._file_loader import decompress_stream, download_file_byte_stream
from package_statistics._formatter import format_stats_output
from package_statistics._parser import parse_package_names
from package_statistics._statistics import count_package_occurrences

__all__ = ["run"]


def run():
    """
    Command that takes the architecture as an argument (amd64, arm64, mips etc.). Downloads the compressed Contents
    file associated with it from a Debian mirror. The program parses the file and outputs the statistics of the
    packages that have the most files associated with them.
    """
    parser = ArgumentParser(description="Package Statistics")
    initialize_parser(parser)

    args: Namespace = parser.parse_args()
    architecture: str = args.architecture
    limit: int = args.limit
    if args.architecture not in SUPPORTED_ARCHITECTURES:
        sys.exit(f"Architecture {architecture} is not in {SUPPORTED_ARCHITECTURES}.")

    file_name: str = CONTENT_FILE_NAME_TEMPLATE.format(architecture=architecture)
    url: str = f"{DEBIAN_STABLE_REPOSITORY_URL}/{file_name}"

    stream: BytesIO = download_file_byte_stream(url)
    decompressed: str = decompress_stream(stream)
    parsed: list[str] = parse_package_names(decompressed)
    package_stats: list[tuple[str, int]] = count_package_occurrences(
        parsed, limit=limit
    )
    output: str = format_stats_output(
        package_stats, title_fill_char="-", title_text="PACKAGE STATISTICS"
    )
    sys.stdout.write(output)
