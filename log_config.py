import logging
import os


logger = logging.getLogger("Profit/Loss Simulation")
FILE_FORMAT = '[%(asctime)s] - [%(levelname)s] - [%(filename)s] - [%(funcName)s()] - [%(lineno)d] - %(message)s'
CONSOLE_FORMAT = '[%(levelname)s] - [%(filename)s] - [%(funcName)s()] - [%(lineno)d] - %(message)s'


def get_logger(base_dir):
    time_str = open(os.path.join(base_dir, 'parameters', 'run_id.txt')).read().strip()
    file_logger_format = logging.Formatter(FILE_FORMAT)
    console_logger_format = logging.Formatter(CONSOLE_FORMAT)
    logger_file = os.path.join(base_dir, f'logging_files', f'Run_{time_str}.log')
    if not os.path.isfile(logger_file):
        os.makedirs(os.path.split(logger_file)[0], exist_ok=True)
        os.system(f'touch {logger_file}')
    file_logger = logging.FileHandler(logger_file, mode='a')
    file_logger.setFormatter(file_logger_format)
    logger.addHandler(file_logger)
    logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler()
    console.setFormatter(console_logger_format)
    logger.addHandler(console)
    console.setLevel(logging.INFO)

    return logger


logger_run = get_logger(base_dir='.')
