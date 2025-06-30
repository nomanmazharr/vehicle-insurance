import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

log_dir = 'logs'
log_file = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
Max_log_size = 5*1024*1024
backup = 3

log_dir_path = os.path.join(from_root(), log_dir)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, log_file)

def configure_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    filehandler = RotatingFileHandler(log_file_path, maxBytes=Max_log_size, backupCount=backup)
    filehandler.setFormatter(formatter)
    filehandler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(filehandler)
    logger.addHandler(console_handler)

configure_logger()

