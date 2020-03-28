#!/usr/bin/env python
import pika
import sys
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='general', exchange_type='direct')

message = 'Hello World!'

channel.basic_publish(
    exchange='general', routing_key='profesores', body=message)
print(" [x] Sent %r" % (message))
connection.close()