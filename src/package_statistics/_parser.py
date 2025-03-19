import logging

logger = logging.getLogger(__name__)

__all__ = ["parse_package_names"]

_PACKAGE_DELIMITER = ","


def parse_package_names(content: str) -> list[str]:
    """
    Parse the content of the Contents file and extract package names.

    :param content: The content of the Contents file as a string.
    :return: A list of package names.
    """
    lines: list[str] = content.splitlines()
    package_elements_per_row: list[str] = [line.rpartition(" ")[-1] for line in lines]  # get the last element of each line
    joined_package_names: str = _PACKAGE_DELIMITER.join(package_elements_per_row)
    package_names: list[str] = joined_package_names.split(_PACKAGE_DELIMITER)
    logger.info(f"Parsed content index | Package references: {len(package_names)} |")
    return package_names
