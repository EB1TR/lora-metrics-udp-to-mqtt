# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=W0703

__author__ = 'EB1TR'

import sys
from os import environ, path
from environs import Env


ENV_FILE = path.join(path.abspath(path.dirname(__file__)), '.env')

try:
    ENVIR = Env()
    ENVIR.read_env()
except Exception as e:
    print('Error: .env file not found: %s' % e)
    sys.exit(1)


class Config:
    """
    This is the generic loader that sets common attributes

    :param: None
    :return: None
    """

    if environ.get('UDP_PORT'):
        UDP_PORT = int(ENVIR('UDP_PORT'))

    if environ.get('UDP_IP'):
        UDP_IP = ENVIR('UDP_IP')

    if environ.get('MQTT_HOST'):
        MQTT_HOST = ENVIR('MQTT_HOST')

    if environ.get('MQTT_PORT'):
        MQTT_PORT = int(ENVIR('MQTT_PORT'))

    if environ.get('MQTT_TOPIC'):
        MQTT_TOPIC = ENVIR('MQTT_TOPIC')
