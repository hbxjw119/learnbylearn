#/usr/local/bin/python2.7
# -*- coding:utf-8 -*-
import sys, json, pika, traceback

def msg_rcvd(channel, method, header, body):
    message = json.loads(body)

    print 'received %(content)s /%(time)d' % message
    channel.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    AMQP_SERVER = sys.argv[1]
    AMQP_PORT = int(sys.argv[2])

    USER = sys.argv[3]
    PASS = sys.argv[4]

    creds_broker = pika.PlainCredentials(USER, PASS)
    conn_params = pika.ConnectionParameters(AMQP_SERVER, AMQP_PORT, '/', creds_broker)

    while True:
        try:
            conn_broker = pika.BlockingConnection(conn_params)

            channel = conn_broker.channel()
            channel.exchange_declare('cluster_test',exchange_type='direct',auto_delete=False)
            channel.queue_declare('cluster_test',auto_delete=False)
            channel.queue_bind(queue='cluster_test',exchange='cluster_test',routing_key='cluster_test')

            print 'Ready for testing!'
            channel.basic_consume(msg_rcvd,queue='cluster_test',no_ack=False,consumer_tag='cluster_test')
            channel.start_consuming()
        except Exception, e:
            traceback.print_exc()
