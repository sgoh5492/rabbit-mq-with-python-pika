#!/usr/bin/env python
import pika
import sys
connectionParam = pika.ConnectionParameters( host = 'localhost' )
connection = pika.BlockingConnection( connectionParam )
channel = connection.channel()

channel.exchange_declare( exchange = 'logs', type = 'fanout' )

message = ' '.join( sys.argv[1:] ) or 'info: Hello World!'

channel.basic_publish(
		exchange = 'logs',
        routing_key = '',
		body = message
	)

print " [x] Sent %r" % ( message, )

connection.close()