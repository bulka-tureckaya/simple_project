from loguru import logger

logger.add("app.log", rotation="500 MB", level="INFO")
