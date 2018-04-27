import pika,sys

#credentials = pika.PlainCredentials('guest','guest')
#con = pika.ConnectionParameters('localhost',credentials=credentials)

credentials = pika.PlainCredentials('test','test')
con = pika.ConnectionParameters('10.96.96.31',5672,credentials=credentials)

con_broker = pika.BlockingConnection(con)

channel = con_broker.channel()
channel.exchange_declare(exchange='hello-exchange',exchange_type='direct',passive=False,durable=True,auto_delete=False)

channel.queue_declare(queue='hello-queue')
channel.queue_bind(queue='hello-queue',exchange='hello-exchange',routing_key='hola')

def msg_consumer(channel, method, header, body):
	channel.basic_ack(delivery_tag=method.delivery_tag)
	if body == 'quit':
		channel.basic_cancel(consumer_tag='hello-consumer')
		channel.stop_consuming()
	else:
		print body
	return 

channel.basic_consume(msg_consumer, queue='hello-queue',consumer_tag='hello-consumer')
channel.start_consuming()
