import logging
import os
from logging.handlers import RotatingFileHandler

if not os.path.exists('logs'):
    os.makedirs('logs')

def setup_logger():
    logger = logging.getLogger("chat_logger")
    logger.setLevel(logging.DEBUG)  # Capture todos los niveles de logs

    # Crear un manejador de archivo que rotará los logs
    file_handler = RotatingFileHandler("logs/chat.log", maxBytes=1000000, backupCount=3)
    file_handler.setLevel(logging.DEBUG)  # Captura todos los niveles de logs en archivo

    # Crear un formateador y añadirlo al manejador
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Añadir el manejador al logger
    logger.addHandler(file_handler)

    # Opcional: Crear un manejador para CRITICAL logs para notificaciones
    critical_handler = RotatingFileHandler("logs/critical.log", maxBytes=1000000, backupCount=3)
    critical_handler.setLevel(logging.CRITICAL)
    critical_handler.setFormatter(formatter)
    logger.addHandler(critical_handler)

    return logger

# Configurar el logger globalmente
logger = setup_logger()