"""
Wraps Python's ``logging`` with the default settings.
"""

import os
import logging
from ocspd.colourlog import ColourFormatter

#: :attr:`logging.format` format string for log files and syslog
LOGFORMAT = '[%(levelname)s] %(threadName)+10s/%(name)-16.20s %(message)s'
#: :attr:`logging.format` format string for stdout
COLOUR_LOGFORMAT = (
    '{lvl}[%(levelname)s]{reset} {msg}%(threadName)+10s/%(name)-16.20s '
    '%(message)s{reset}'
)

def get_logger(*args, **kwargs):
    """
    Wraps logging.getLogger (note the camel case, ew.), also provided for
    consistency.
    :param *args args: Positional arguments for ``logger.getLogger``.
    :param *kwargs kwargs: Keyword arguments for ``logger.getLogger``.
    """
    logger = logging.getLogger(*args, **kwargs)
    return logger


def set_logger(name, logdir=False, verbose=0, quiet=False, syslog=False):
    """
    Wraps logging.getLogger (note the camel case, ew.), and applies the default
    logging settings. Do this once when initialising your application.

    :param mixed logdir: False to disable logging to files, a str path to
        enable and to indicate where to log to.
    :param int verbose: How verbose should the output be, hint: you should
        pass a ``argparser`` ``narg`` type to this, so -v equals 1, --vv
        equals 2, etc.
    :param bool quiet: Don't output to stdout.
    :param bool syslog: Don't output to syslog.
    """
    # Keep track of my filehandles
    log_file_handles = []
    log_level = max(min(50 - verbose * 10, 50), 10)
    logging.basicConfig()
    log = logging.getLogger(name)
    log.propagate = False
    log.setLevel(level=log_level)
    if not quiet:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(
            ColourFormatter(COLOUR_LOGFORMAT)
        )
        log.addHandler(console_handler)
    if logdir:
        file_handler = logging.FileHandler(
            os.path.join(logdir, 'ocspd.log'))
        file_handler.setLevel(log_level)
        file_handler.setFormatter(logging.Formatter(LOGFORMAT))
        log.addHandler(file_handler)
        log_file_handles.append(file_handler.stream)
    if syslog:
        syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')
        syslog_handler.setLevel(log_level)
        syslog_handler.setFormatter(logging.Formatter(LOGFORMAT))
        log.addHandler(syslog_handler)

    # Don't allow dependencies to log anything but fatal errors
    logging.getLogger("requests").setLevel(logging.FATAL)
    logging.getLogger("urllib3").setLevel(logging.FATAL)
    return log
