# coding=utf-8
import pika
import os
from main.config import config_env


def get_conn():
    url = os.environ.get('CLOUDAMQP_URL', config_env.get("AMQP_URL"))
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    return connection


class Publisher:

    def __init__(self):
        self.__connection = get_conn()
        self.__channel = self.__connection.channel()

    def close_connection(self):
        self.__connection.close()

    def send_by_direct_exchange(self, exchange, routing_key, messages):
        channel = self.__channel
        channel.exchange_declare(exchange=exchange, exchange_type='direct')
        for message in messages:
            print("Sent msg: {} routing_key: {}".format(message, routing_key))
            channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message,
                                  properties=pika.BasicProperties(
                                      delivery_mode=2,  # make message persistent
                                  ))


class Consumer:
    def __init__(self):
        self.__connection = get_conn()
        self.__channel = self.__connection.channel()

    def receive_by_direct_exchange(self, exchange, routing_key, callback, queue_name):
        channel = self.__channel
        channel.exchange_declare(exchange=exchange, exchange_type='direct')
        channel.queue_declare(queue=queue_name, durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_key)
        channel.basic_consume(callback, queue=queue_name)
        print('Starting to receive messages from queue: {}'.format(queue_name))
        channel.start_consuming()
