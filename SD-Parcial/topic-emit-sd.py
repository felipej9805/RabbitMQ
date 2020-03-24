#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('root','password')

connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.0.10', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic-messages', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'

message = ' '.join(sys.argv[2:]) or 'Hola a todos'

channel.basic_publish(
    exchange='topic-messages', routing_key=routing_key, body=message)

print(" [x] Enviado %r:%r" % (routing_key, message))

connection.close()
