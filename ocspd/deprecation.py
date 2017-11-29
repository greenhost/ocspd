"""
Output a warning message about the deprecation of this version of the project.
"""

import datetime
import logging

LOG = logging.getLogger(__name__)


def run(setup=False):
    def log(msg, level):
        if not setup:
            LOG.log(level, msg)
        else:
            level = logging._levelNames[level]
            print("{level}: {msg}".format(level=level, msg=msg))

    def warning(msg):
        log(msg, logging.WARNING)

    def error(msg):
        log(msg, logging.ERROR)

    def critical(msg):
        log(msg, logging.CRITICAL)

    critical_date = datetime.date(2018, 6, 30)
    error_date = datetime.date(2018, 1, 1)
    today = datetime.date.today()
    msg = (
        "\n======= IMPORTANT NOTICE =======\n"
        "This project was renamed to `stapled`. If you still rely on this "
        "repo, you should change your configuration to use our renamed "
        "daemon. You can find it at: https://github.com/greenhost/stapled\n"
        "================================"
    )

    if today > critical_date:
        critical(msg)
        if setup:
            critical(
                "Installation of this package will be canceled, sorry "
                "for the inconvenience."
            )
            exit(1)
    elif today > error_date:
        error(msg)
    else:
        warning(msg)
