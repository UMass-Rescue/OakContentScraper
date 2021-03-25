from loguru import logger
import sys


def setup_logging():
    logger.remove()
    logger.add(
        sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO"
    )
    logger.add(
        sys.stdout,
        colorize=True,
        format="<green>{time}</green> <level>{message}</level>",
    )
    # logger.add("content_scraper_{time}.log")
