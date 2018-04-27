import pika,sys
from pika import spec

#credentials = pika.PlainCredentials('guest','guest')
#con = pika.ConnectionParameters('localhost',credentials=credentials)

credentials = pika.PlainCredentials('test','test')
con = pika.ConnectionParameters('10.96.96.31',5672,credentials=credentials)

con_broker = pika.BlockingConnection(con)

channel = con_broker.channel()

def confirm_handler(frame):
    if type(frame.method) == spec.Confirm.SelectOk:
        print 'channel in confirm mode'
    elif type(frame.method) == spec.Basic.Nack:
        if frame.method.delivery_tag in msg_ids:
            print 'message lost'
    elif type(frame.method) == spec.Basic.Ack:
        if frame.method.delivery_tag in msg_ids:
            print 'confirm received'
            msg_ids.remove(frame.method.delivery_tag)
channel.confirm_delivery()

#channel.exchange_declare(exchange='hello-exchange',exchange_type='direct',passive=False,durable=True,auto_delete=False)

msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = 'text/plain'

msg_ids = []

if channel.basic_publish(body=msg,exchange='hello-exchange',properties=msg_props,routing_key='hola'):
    print 'confirm received'
else:
    print 'message lost'
msg_ids.append(len(msg_ids) + 1)
channel.close()
