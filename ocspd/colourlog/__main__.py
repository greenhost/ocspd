# -*- coding: utf-8 -*-
"""
Test the ColourFormatter class when run directly.
"""
import logging
import ocspd.core.log
from ocspd.colourlog import ColourFormatter


def main():
    """
    Test the ColourFormatter class when run directly.
    """

    logger = ocspd.core.log.get_logger(__name__)

    logger.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = ColourFormatter(
        "{lvl}[%(levelname)s]{reset} - {msg}%(asctime)-15s %(name)s "
        "%(message)s{reset}"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.debug("This is detailed information..")
    logger.info("This somewhat more useful..")
    logger.warning("This might be dangerous..")
    logger.error("Something might have gone a bit wrong")
    logger.critical("Woah! do something!!")


if __name__ == '__main__':
    main()
