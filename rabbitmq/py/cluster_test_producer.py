#/usr/local/bin/python2.7
# -*- coding:utf-8 -*-
import sys, json, pika, time

if __name__ == '__main__':
    AMQP_SERVER = sys.argv[1]
    AMQP_PORT = int(sys.argv[2])

    USER = sys.argv[3]
    PASS = sys.argv[4]
    creds_broker = pika.PlainCredentials(USER, PASS)
    conn_params = pika.ConnectionParameters(AMQP_SERVER, AMQP_PORT, '/', creds_broker)

    conn_broker = pika.BlockingConnection(conn_params)

    channel = conn_broker.channel()
    msg = json.dumps({'content': 'cluster test msg!', 'time': time.time()})
    msg_props = pika.BasicProperties(content_type='application/json')
    channel.basic_publish(body=msg, exchange='cluster_test',properties=msg_props,routing_key='cluster_test')

    print 'send cluster test message'
