from collections import Counter
import logging

logger = logging.getLogger(__name__)

__all__ = ["count_package_occurrences"]


def count_package_occurrences(parsed: list[str], limit: int) -> list[tuple[str, int]]:
    """
    Count the occurrences of each package in the parsed list.

    :param parsed: List of package names.
    :param limit: The maximum number of packages included in the output.
    """
    counter = Counter(parsed)
    package_stats: list[tuple[str, int]] = counter.most_common(limit)
    logger.info("Counted package occurrences")
    return package_stats
