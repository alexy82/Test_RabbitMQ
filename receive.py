import pika
import os
import config


class Consume:
    @staticmethod
    def receive_by_direct_exchange(exchange, routing_key, callback):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='direct')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_key)
        channel.basic_consume(callback, queue=queue_name, no_ack=True)
        print('Start receive message from queue: {}'.format(queue_name))
        channel.start_consuming()


def callback(ch, method, pros, body):
    print('Receive msg: {}'.format(body))


exchange = 'test'
routing_key = 'test' or 'rabbitMQ'
Consume.receive_by_direct_exchange(exchange, routing_key, callback)
