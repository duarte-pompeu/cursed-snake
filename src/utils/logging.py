import functools

from loguru import logger

logger.add("logs/file_1.log/", retention="100 days")
