from main.my_rabbitmq import Consumer


def callback(ch, method, pros, body):
    print('Receive msg: {}'.format(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)


exchange = 'test'
routing_key = 'test'
queue_name = 'queue'+routing_key
consumer = Consumer()
consumer.receive_by_direct_exchange(exchange, routing_key, callback, queue_name)
