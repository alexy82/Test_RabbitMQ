import pika
import os
from main.config.config_env import Config


# Make sure only a connection open during project
class ConnectionManager(object):
    __connection = None

    @staticmethod
    def reset_conn():
        url = os.environ.get('CLOUDAMQP_URL', Config.get(Config.AMQP_URL))
        params = pika.URLParameters(url)
        ConnectionManager.__connection = pika.BlockingConnection(params)

    @staticmethod
    def get_conn():
        ConnectionManager.check_connect()
        return ConnectionManager.__connection

    @staticmethod
    def close_conn():
        ConnectionManager.__connection.close()

    @staticmethod
    def get_channel():
        return ConnectionManager.get_conn().channel()

    # Check connect if connect is closed, creating new connection
    @staticmethod
    def check_connect():
        if (ConnectionManager.__connection == None or ConnectionManager.__connection.is_closed):
            ConnectionManager.reset_conn()
            return False
        return True
