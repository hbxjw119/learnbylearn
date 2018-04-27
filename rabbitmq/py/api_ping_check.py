#/usr/local/bin/python2.7
# -*- coding:utf-8 -*-
import sys, httplib, urllib, base64, socket

EXIT_OK = 0
EXIT_WARNING = 1
EXIT_CRITICAL = 2
EXIT_UNKNOWN = 3


if __name__ == '__main__':
    AMQP_SERVER = sys.argv[1]
    AMQP_PORT = int(sys.argv[2])
    VHOST = sys.argv[3]

    USER = sys.argv[4]
    PASS = sys.argv[5]

    conn = httplib.HTTPConnection(AMQP_SERVER, AMQP_PORT)
    path = '/api/aliveness-test/%s' % urllib.quote(VHOST, '')
    method = 'GET'
    credentials = base64.b64encode('%s:%s' % (USER, PASS))

    try:
        conn.request(method, path, '', {'Content-Type': 'application/json', 'Authorization': 'Basic ' + credentials})
    except socket.error:
        print 'CRITICAL: Could not connect to %s: %s!' % (AMQP_SERVER, AMQP_PORT)
        exit(EXIT_CRITICAL)

    response = conn.getresponse()

    if response.status > 299:
        print 'CRITICAL: Broker not alive: %s' % response.read()
        exit(EXIT_CRITICAL)

    print 'OK: Broker is alive: %s' % response.read()
    exit(EXIT_OK)
