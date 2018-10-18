# coding=utf-8

import os
import json

# Prepare Object save content from file Json
''' 
Each of Exchanges is a object which have name and  a dictionary has key = routing_key and value = array of message
'''


class Exchange(object):
    __exchange = ''
    __routing_keys = {}

    def __init__(self, exchange):
        self.__exchange = exchange

    def get_exchange(self):
        return self.__exchange

    def get__routing_key(self):
        return self.__routing_keys

    def add_message(self, routing_key, message):
        self.__routing_keys.update({routing_key: message})


class JsonProcess(object):
    @staticmethod
    def get_routing_key(exchange):
        files = os.listdir(exchange)
        routing_keys = []
        for i in files:
            if i.count('.json') == 1:
                routing_keys.append(i.split('.')[0])
        return routing_keys

    @staticmethod
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

    @staticmethod
    def read_json(path):
        with open(path) as json_data:
            d = json.load(json_data)
        return d

    @staticmethod
    def fill_exchange(path, exchange):
        routing_keys = JsonProcess.get_routing_key(path)
        for routing_key in routing_keys:
            json_path = '{}/{}.{}'.format(path, routing_key, 'json')
            messages = [str(message) for message in JsonProcess.read_json(json_path)]
            exchange.add_message(routing_key, messages)

    @staticmethod
    def convert_json_to_message(exchange_path):
        exchanges = JsonProcess.get_exchange(exchange_path)
        exchange_list = []
        for exchange in exchanges:
            exchange_object = Exchange(exchange)
            path = '{}/{}'.format(exchange_path, exchange)
            JsonProcess.fill_exchange(path, exchange_object)
            exchange_list.append(exchange_object)
        return exchange_list
