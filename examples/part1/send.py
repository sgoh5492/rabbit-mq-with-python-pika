#!/usr/bin/env python
from datetime import datetime
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue = 'hello')
channel.basic_publish(exchange = '',
		routing_key = 'hello',
		body = 'msg at ' + str(datetime.now())
	)
print " [x] Sent 'Hello World!'"
connection.close()