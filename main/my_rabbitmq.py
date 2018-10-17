# coding=utf-8
import pika
import os
from main.config import config_env


class MessageBroker:
    @staticmethod
    def get_connection():
        url = os.environ.get('CLOUDAMQP_URL', config_env.get("AMQP_URL"))
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        return connection

    @staticmethod
    def sent_by_direct_exchange( exchange, routing_key, messages):
        connection = MessageBroker.get_connection()
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='direct')
        for message in messages:
            print("Sent msg: {} routing_key: {}".format(message, routing_key))
            channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)
        connection.close()

    @staticmethod
    def receive_by_direct_exchange( exchange, routing_key, callback):
        connection = MessageBroker.get_connection()
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='direct')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_key)
        channel.basic_consume(callback, queue=queue_name, no_ack=True)
        print('Start receive message from queue: {}'.format(queue_name))
        channel.start_consuming()
