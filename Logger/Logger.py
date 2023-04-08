import logging


class Logger:
    def __init__(self):
        self.__logger = logging.getLogger()
        self.__logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler("atto_reports_automation.log")
        self.__logger.addHandler(file_handler)

    def get_logger(self):
        return self.__logger
