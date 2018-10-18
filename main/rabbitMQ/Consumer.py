from main.rabbitMQ.ConnectionManager import ConnectionManager


class Consumer(object):
    __channel = None
    __exchange = ''
    __routing_key = ''
    __queue = ''
    __callback = None

    def __init__(self, exchange, routing_key, queue, callback):
        self.__exchange = exchange
        self.__routing_key = routing_key
        self.__queue = queue
        self.__callback = callback
        self.__setting()

    # Setting environment(declare) before consuming
    def __setting(self):
        self.__channel = ConnectionManager.get_channel()
        self.__channel.exchange_declare(exchange=self.__exchange, exchange_type='topic')
        self.__channel.queue_declare(queue=self.__queue, durable=True)
        self.__channel.basic_qos(prefetch_count=1)
        self.__channel.queue_bind(exchange=self.__exchange, queue=self.__queue, routing_key=self.__routing_key)

    def start_consuming(self):
        # Always Make sure the opening connection
        if not ConnectionManager.check_connect():
            self.__channel = ConnectionManager.get_channel()
            self.__setting()
        channel = self.__channel
        channel.basic_consume(self.__callback, queue=self.__queue)
        channel.start_consuming()
