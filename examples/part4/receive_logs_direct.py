#!/usr/bin/env python
import pika
import sys
import time

param = pika.ConnectionParameters( host = 'localhost' )
connection = pika.BlockingConnection( param )
channel = connection.channel()

channel.exchange_declare( exchange = 'direct_logs', type = 'direct' )

result = channel.queue_declare( exclusive = True )
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    print >> sys.stderr, "Usage: %s [info] [warning] [error]" % ( sys.argv[0], )
    sys.exit(1)

for severity in severities:
    channel.queue_bind(
        exchange = 'direct_logs',
        queue = queue_name,
        routing_key = severity )

def callback( ch, method, properties, body ):
    for i in range(3) :
        print " [progress] %d/3" % ( i )
        time.sleep( 1 )
    print " [x] %r:%r" % ( method.routing_key, body, )

channel.basic_consume( callback, queue = queue_name, no_ack = True )

print ' [*] Waiting for logs. To exit press CTRL+C'

channel.start_consuming()