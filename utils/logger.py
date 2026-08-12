import logging
import os

os.makedirs("logs",exist_ok=True)

def get_logger(name):
    logger = logging.getLogger(name)
    logging.basicConfig(
        level=logging.DEBUG,
        format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%d-%m-Y %H:%M:%S",
        handlers=[logging.FileHandler(filename="logs/app.log"),
                  logging.StreamHandler()]
    )
    return logger