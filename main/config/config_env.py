from dotenv import load_dotenv
import os

load_dotenv()


class Config(object):
    AMQP_URL = "AMQP_URL"
    EXCHANGE_DIRECTORY = "EXCHANGE_DIR"

    @staticmethod
    def get(key):
        return os.getenv(key)
