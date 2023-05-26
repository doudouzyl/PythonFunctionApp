import logging

import azure.functions as func

from azure.servicebus import ServiceBusClient
from azure.servicebus.amqp import AmqpAnnotatedMessage, AmqpMessageBodyType
import requests
import uamqp
from uamqp import types as uamqp_types, utils, authentication, constants


def main(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))
