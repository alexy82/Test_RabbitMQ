import pika
import os
import json
import config


class Publish:

    # Gửi message
    @staticmethod
    def __sent_by_direct_exchange(exchange, routing_key, messages):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='direct')
        for message in messages:
            print("Sent msg: {} routing_key: {}".format(message, routing_key))
            channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)
        connection.close()

    # Lấy tất cả tên file json (routing_key)
    @staticmethod
    def __get_routing_key(exchange):
        files = os.listdir(exchange)
        routing_keys = []
        for i in files:
            if i.count('.json') == 1:
                routing_keys.append(i.split('.')[0])
        return routing_keys

    # Lấy tất cả exchange
    @staticmethod
    def __get_exchange(exchange_path):
        files = os.listdir(exchange_path)
        exchanges = []
        for i in files:
            if os.path.isdir('{}/{}'.format(exchange_path, i)):
                exchanges.append(i)

        return exchanges

    # Đọc Json
    @staticmethod
    def __read_json(path):
        print('Open file Json {}'.format(path))
        with open(path) as json_data:
            d = json.load(json_data)
        return d

    @staticmethod
    def __sent_to_exchange(path, exchange):
        files = Publish.__get_routing_key(path)
        for file in files:
            json_path = '{}/{}.{}'.format(path, file, 'json')
            messages = [str(message) for message in Publish.__read_json(json_path)]
            Publish.__sent_by_direct_exchange(exchange, file, messages)

    @staticmethod
    def sent(exchange_path):
        exchanges = Publish.__get_exchange(exchange_path)
        for exchange in exchanges:
            path = '{}/{}'.format(exchange_path, exchange)
            print("Start sent msg to exchange: {}".format(exchange))
            Publish.__sent_to_exchange(path, exchange)


__exchange = config.get('EXCHANGE_DIR')
Publish.sent(__exchange)
