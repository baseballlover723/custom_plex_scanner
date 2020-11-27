# -*- coding: utf-8 -*-

import os
import inspect
import logging
import sys
from abc import ABC


class BaseScanner(ABC):
    def __init__(self):
        self.plex_root = os.path.abspath(
            os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), "..", ".."))
        self.logging_directory = f"{self.plex_root}/Logs/{self.scanner_name()}"
        os.makedirs(self.logging_directory, exist_ok=True)
        logfile_path = f"{self.logging_directory}/log.log"

        logging.basicConfig(filename=logfile_path, encoding="utf-8", level=logging.DEBUG)
        logging.info(f"Starting scan with args: {sys.argv}")

    def scanner_name(self):
        return self.__class__.__name__
