#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('kelvin','asdf1024')
connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='localhost', credentials=credentials ))
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'
def callback(ch, method, properties, body):
	print " [x] Received %r" % (body,)

channel.basic_consume(callback,
		queue='hello',
		no_ack=True)
channel.start_consuming()
