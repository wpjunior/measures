import socket
import json
import time


class Measure(object):

    def __init__(self, client, address):
        self.client = client
        self.address = address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def count(self, metric, counter=1, dimensions={}):
        message = {
            'client': self.client,
            'metric': metric,
            'count': counter,
        }
        message = dict(dimensions.items() + message.items())
        self.socket.sendto(json.dumps(message), self.address)