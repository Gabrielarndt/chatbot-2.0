import logging

def setup_logging():
    
    logger = logging.getLogger('flask_app')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('flask.log')
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
