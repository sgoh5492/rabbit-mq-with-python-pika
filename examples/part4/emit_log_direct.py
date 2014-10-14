#!/usr/bin/env python
import pika
import sys

param = pika.ConnectionParameters( host = 'localhost' )
connection = pika.BlockingConnection( param )
channel = connection.channel()

channel.exchange_declare( exchange = 'direct_logs', type = 'direct' )

severity = sys.argv[1] if len( sys.argv ) > 1 else 'info'
message = ' '.join( sys.argv[2:] ) or 'Hello World!'

channel.basic_publish(
		exchange = 'direct_logs',
		routing_key = severity,
		body = message )

print " [x] Sent %r:%r" % ( severity, message )

connection.close()