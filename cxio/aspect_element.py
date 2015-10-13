__author__ = 'cmzmasek'

import json
import ijson


class AspectElement(object):

    def __init__(self, name, data=None):
        self.name = name
        self.data = data

    def to_json(self):
        return json.dumps(self.data)

    def get_name(self):
        return self.name

    def get_data(self):
        return self.data

    def __str__(self):
        return str(self.name) + ': ' + str(self.data)


