from typing import Final, FrozenSet

__all__ = [
    "SUPPORTED_ARCHITECTURES",
    "DEBIAN_STABLE_REPOSITORY_URL",
    "CONTENT_FILE_NAME_TEMPLATE",
]

SUPPORTED_ARCHITECTURES: Final[FrozenSet[str]] = frozenset(
    {
        "amd64",
        "arm64",
        "armel",
        "armhf",
        "i386",
        "mips64el",
        "mipsel",
        "ppc64el",
        "s390x",
    }
)

DEBIAN_STABLE_REPOSITORY_URL: Final[str] = "http://ftp.uk.debian.org/debian/dists/stable/main"

CONTENT_FILE_NAME_TEMPLATE: Final[str] = "Contents-{architecture}.gz"
