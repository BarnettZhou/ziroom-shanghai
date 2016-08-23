# some methods

import os
import json


def readConfig(config_type):
    with open(os.path.dirname(__file__) + '/../config/' + config_type + '.json', 'rb') as config_file:
        config = json.loads(config_file.read())
    return config


def weiteErrorLog(file, content):
    return 0
