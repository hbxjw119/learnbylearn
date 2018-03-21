#/usr/local/bin/python2.7
# -*- coding:utf-8 -*-
import sys, json, pika, time, traceback

EXIT_OK = 0
EXIT_WARNING = 1
EXIT_CRITICAL = 2
EXIT_UNKNOWN = 3


if __name__ == '__main__':
    AMQP_SERVER = sys.argv[1]
    AMQP_PORT = int(sys.argv[2])

    USER = sys.argv[3]
    PASS = sys.argv[4]

    creds_broker = pika.PlainCredentials(USER, PASS)
    conn_params = pika.ConnectionParameters(AMQP_SERVER, AMQP_PORT, '/', creds_broker)

    try:
        conn_broker = pika.BlockingConnection(conn_params)
        channel = conn_broker.channel()

    except Exception:

        print 'CRITICAL: Could not connect to %s: %s!' % (AMQP_SERVER, AMQP_PORT)
        exit(EXIT_CRITICAL)

    print 'OK: Connect to %s: %s successful.' % (AMQP_SERVER, AMQP_PORT)
