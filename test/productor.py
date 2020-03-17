#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#Exchange: De un lado recibe mensajes del productor y del otro lado los empuja en una cola
channel.exchange_declare(exchange='mensajes', 
    exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'

message = ' '.join(sys.argv[2:]) or 'Saludos a todos'

channel.basic_publish(
    exchange='mensajes', routing_key=severity, body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()