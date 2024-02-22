import logging

def setup_logging():
    # Configuração do logger
    logger = logging.getLogger('flask_app')
    logger.setLevel(logging.DEBUG)

    # Criação de um manipulador para registrar mensagens em um arquivo
    file_handler = logging.FileHandler('flask.log')
    file_handler.setLevel(logging.DEBUG)

    # Formato para as mensagens de registro
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Adiciona o manipulador ao logger
    logger.addHandler(file_handler)
