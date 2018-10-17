# coding=utf-8

import os
import json
from main.config import config_env


def get_routing_key(exchange):
    files = os.listdir(exchange)
    routing_keys = []
    for i in files:
        if i.count('.json') == 1:
            routing_keys.append(i.split('.')[0])
    return routing_keys


def get_exchange(exchange_path):
    if (os.path.isdir(exchange_path)):

        files = os.listdir(exchange_path)
        exchanges = []
        for i in files:
            if os.path.isdir('{}/{}'.format(exchange_path, i)):
                exchanges.append(i)

        return exchanges
    else:
        return []


def read_json(path):
    print('Open file Json {}'.format(path))
    with open(path) as json_data:
        d = json.load(json_data)
    return d


def send_to_exchange(path, exchange):
    files = get_routing_key(path)
    for file in files:
        json_path = '{}/{}.{}'.format(path, file, 'json')
        messages = [str(message) for message in read_json(json_path)]
        from main.my_rabbitmq import Publisher
        publisher = Publisher()
        publisher.send_by_direct_exchange(exchange, file, messages)


def send(exchange_path):
    exchanges = get_exchange(exchange_path)
    for exchange in exchanges:
        path = '{}/{}'.format(exchange_path, exchange)
        print("Start sent msg to exchange: {}".format(exchange))
        send_to_exchange(path, exchange)


send(config_env.get("EXCHANGE_DIR"))
