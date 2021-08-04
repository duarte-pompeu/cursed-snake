from loguru import logger


def init():
    logger.add("logs/file_1.log/", retention="100 days")
