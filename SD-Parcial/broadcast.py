#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='broadcast', exchange_type='fanout')

message = "Hello World!"
channel.basic_publish(exchange='broadcast', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()