from typing import Final
import logging

logger = logging.getLogger(__name__)

__all__ = ["format_stats_output"]


_OFFSET: Final[int] = 1
NUM_COLUMNS: Final[int] = 3


def format_stats_output(
    package_stats: list[tuple[str, int]], title_text: str, title_fill_char: str
) -> str:
    """
    Format the package statistics output.

    :param package_stats: List of tuples containing package names and their counts.
    :param title_text: Title text for the output.
    :param title_fill_char: Character used to fill the title boundaries.
    :return: Formatted string of package statistics.
    """

    max_rank: int = len(package_stats)
    max_rank_width: int = len(str(max_rank)) + _OFFSET
    max_package_width: int = max(len(stat[0]) for stat in package_stats)
    max_count_width: int = len(str(package_stats[0][1]))
    max_row_width: int = (
        max_rank_width + max_package_width + max_count_width + (_OFFSET * NUM_COLUMNS)
    )

    title: str = "{title:{fill}{align}{width}}".format(
        title=title_text, fill=title_fill_char, align="^", width=max_row_width
    )
    header: str = (
        "{rank_header:<{r_width}} {package_header:<{p_width}}  {count_header}".format(
            rank_header="",
            r_width=max_rank_width,
            package_header="Package",
            p_width=max_package_width,
            count_header="Files",
        )
    )
    header_separator: str = "-" * len(header)
    result: str = f"\n{title}\n{header}\n{header_separator}\n"

    for rank, (package, count) in enumerate(package_stats, start=_OFFSET):
        result += (
            "{rank:<{max_rank_width}} {package:<{max_package_width}}  {count}\n".format(
                rank=str(rank) + ".",
                max_rank_width=max_rank_width,
                package=package,
                max_package_width=max_package_width,
                count=count,
            )
        )

    logger.info("Formatted stats output")
    return result
