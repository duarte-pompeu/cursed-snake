from loguru import logger

import functools

logger.add("logs/file_1.log/", retention="100 days")