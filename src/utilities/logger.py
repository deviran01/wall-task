import logging
import os


class Logger:
    @staticmethod
    def get_logger(name: str):
        logger = logging.getLogger(name)
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        logger.setLevel(log_level)
        console_handler = logging.StreamHandler()
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        formatter = logging.Formatter(log_format)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        return logger
