from main.my_rabbitmq import MessageBroker


def callback(ch, method, pros, body):
    print('Receive msg: {}'.format(body))


exchange = 'test'
routing_key = 'rabbitMQ'
MessageBroker.receive_by_direct_exchange(exchange, routing_key, callback)
