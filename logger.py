########################################################################
# Copyright :  © MhdTOUAHRI
#
# 
#
# 
# 
########################################################################

"""
Logger
*******

:module: logger

:synopsis: Basis for implementing a runtime log.

.. currentmodule:: logger
"""

import logging
import time
from pathlib import Path


class BasicLog:
    """Basic implementation of native python logging."""

    @classmethod
    def initialize_logging(
        cls, stout_flag: bool = False, save_flag: bool = False
    ) -> logging.Logger:
        """Initialisation of object logging with configuration of stout and file
        log activation.

        :param stout_flag: Terminal log print activation flag.
        :param save_flag: Log file activation flag.
        :return: Configured logger
        """
        root_logger = logging.getLogger()
        log_format = logging.Formatter(
            "[%(asctime)s.%(msecs)03d] - %(levelname)-8s - %(message)-s (%(filename)s:%(lineno)s)",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        if stout_flag:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(log_format)
            root_logger.addHandler(console_handler)

        if save_flag:
            filename = cls._create_parent_folder()
            file_handler = logging.FileHandler(filename=filename, mode="w")
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(log_format)
            root_logger.addHandler(file_handler)

        root_logger.setLevel(logging.DEBUG)

        return logging.getLogger(__name__)

    @staticmethod
    def _create_parent_folder() -> Path:
        """Create the parent folder of the results file in which all
        the records will be placed and provide the file path.

        :return: Filename path.
        """
        date_format = "%Y-%m-%d_%H-%M-%S"
        extension = ".log"
        parent_folder = Path.cwd() / "reports"
        filename = parent_folder / time.strftime(f"log_{date_format}{extension}")

        if not parent_folder.is_dir():
            parent_folder.mkdir(parents=True, exist_ok=True)

        return filename
