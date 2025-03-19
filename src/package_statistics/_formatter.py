from typing import Final
import logging

logger = logging.getLogger(__name__)

__all__ = ["format_stats_output"]


_OFFSET = 1
NUM_COLUMNS: Final[int] = 3


def format_stats_output(
    package_stats: list[tuple[str, int]], title_text: str, title_fill_char: str
) -> str:
    """
    Format the package statistics output.

    Args:
        list[tuple[str, int]]: List of tuples containing package names and their counts.
        limit (int): Limit for the number of packages to display.

    Returns:
        str: Formatted output string.
    """

    max_rank: int = len(package_stats)
    max_rank_width: int = len(str(max_rank)) + _OFFSET
    max_package_width: int = max(len(stat[0]) for stat in package_stats)
    max_count_width: int = len(str(package_stats[0][1]))
    max_row_width: int = (
        max_rank_width + max_package_width + max_count_width + (_OFFSET * NUM_COLUMNS)
    )
    title = "{title:{fill}{align}{width}}".format(
        title=title_text, fill=title_fill_char, align="^", width=max_row_width
    )
    header = (
        "{rank_header:<{r_width}} {package_header:<{p_width}}  {count_header}".format(
            rank_header="",
            r_width=max_rank_width,
            package_header="Package",
            p_width=max_package_width,
            count_header="Files",
        )
    )
    header_separator = "-" * len(header)
    result = f"{title}\n{header}\n{header_separator}\n"

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
