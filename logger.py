import logging


def start_logger():
    logging.basicConfig(filename='log.log',
                        filemode='w',
                        format='%(asctime)s %(levelname)s::%(message)s',
                        level=logging.DEBUG)

def write_log(description: str):
    return logging.debug(description)