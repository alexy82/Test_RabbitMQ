from main.rabbitMQ.ConnectionManager import ConnectionManager
import pika


class Publisher(object):
    __channel = None
    __exchange = ''
    __routing_key = ''

    def __init__(self, exchange, routing_key):
        self.__exchange = exchange
        self.__routing_key = routing_key
        self.__setting()

    # Setting environment(declare) for exchange
    # Get channel from ConnectionManager
    def __setting(self):
        self.__channel = ConnectionManager.get_channel()
        self.__channel.exchange_declare(exchange=self.__exchange, exchange_type='topic')

    def publish(self, body, content_type=None, content_encoding=None, headers=None, delivery_mode=None, priority=None,
                correlation_id=None, reply_to=None, expiration=None, message_id=None, timestamp=None, type=None,
                user_id=None, app_id=None, cluster_id=None):
        # Always Make sure the opening connection
        if not ConnectionManager.check_connect():
            self.__channel = ConnectionManager.get_channel()
            self.__setting()

        channel = self.__channel
        channel.basic_publish(exchange=self.__exchange, routing_key=self.__routing_key, body=body,
                              properties=pika.BasicProperties(content_type=content_type,
                                                              headers=headers,
                                                              content_encoding=content_encoding,
                                                              delivery_mode=delivery_mode,
                                                              priority=priority,
                                                              correlation_id=correlation_id,
                                                              reply_to=reply_to,
                                                              expiration=expiration,
                                                              message_id=message_id,
                                                              timestamp=timestamp,
                                                              type=type,
                                                              user_id=user_id,
                                                              app_id=app_id,
                                                              cluster_id=cluster_id))
