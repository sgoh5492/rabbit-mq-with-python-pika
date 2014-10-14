#!/usr/bin/env python
import pika

connectionParam = pika.ConnectionParameters( host = 'localhost' )
connection = pika.BlockingConnection( connectionParam )
channel = connection.channel()

channel.exchange_declare( exchange = 'logs', type = 'fanout' )

result = channel.queue_declare( exclusive = True )
queue_name = result.method.queue

channel.queue_bind( exchange = 'logs', queue = queue_name )

def callback(ch, method, properties, body):
    print " [x] %r" % (body,)

channel.basic_consume(
		callback,
        queue = queue_name,
        no_ack = True
    )

print ' [*] Waiting for logs. To exit press CTRL+C'

channel.start_consuming()