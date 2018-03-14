import pika,sys

credentials = pika.PlainCredentials('guest','guest')
con = pika.ConnectionParameters('localhost',credentials=credentials)

con_broker = pika.BlockingConnection(con)

channel = con_broker.channel()
channel.exchange_declare(exchange='hello-exchange',exchange_type='direct',passive=False,durable=True,auto_delete=False)

msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = 'text/plain'

channel.basic_publish(body=msg,exchange='hello-exchange',properties=msg_props,routing_key='hola')
