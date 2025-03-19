import urllib.request
import gzip
from io import BytesIO
import logging

logger = logging.getLogger(__name__)

__all__ = ["download_file_byte_stream", "decompress_stream"]


def download_file_byte_stream(url: str) -> BytesIO:
    """
    Download a file from a given URL and return it as a byte stream.

    :param url: The URL of the file to download.
    :return: The byte stream of the downloaded file.
    """
    logger.info(f"Downloading {url} as byte stream...")
    chunk_size: int = 8192
    with urllib.request.urlopen(url) as response:
        stream = BytesIO()
        while chunk := response.read(chunk_size):
            stream.write(chunk)
        stream.seek(0)

    logger.info(f"Download complete! | Size: {stream.getbuffer().nbytes} bytes |")
    return stream


def decompress_stream(stream: BytesIO) -> str:
    """
    Decompress a gzip-compressed byte stream and return the decompressed content as a string.

    :param stream: The byte stream to decompress.
    :return: The decompressed content as a string.
    """
    with gzip.GzipFile(fileobj=stream) as compressed:
        decompressed: bytes = compressed.read()

    logger.info("Decompressed byte stream")
    return decompressed.decode("utf-8")
