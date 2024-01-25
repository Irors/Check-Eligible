from loguru import logger
from sys import stderr


LOG_OUTPUT = "./log/logfile.log"
LOG_ROTATION = "50 MB"


def add_logger(log_output: str = LOG_OUTPUT, log_rotation: str = LOG_ROTATION):
    logger.remove()
    logger.add(
        stderr, diagnose=True,
        format="<bold><blue>{time:HH:mm:ss}</blue> | <level>{level: <8}</level> | <level>{message}</level></bold>"
    )
    logger.add(sink=LOG_OUTPUT, rotation=LOG_ROTATION)
