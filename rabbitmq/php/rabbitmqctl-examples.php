<?php

require_once('../php-amqplib/amqp.inc');
require_once('config/config.php');

//获得信道
$conn = new AMQPConnection(HOST, PORT, USER, PASS);
$channel = $conn->channel();

//声明交换器
$channel->exchange_declare('logs-exchange', 'topic', false, true, false);

//声明队列
$channel->queue_declare('msg-inbox-errors', false, true, false, false);
$channel->queue_declare('msg-inbox-logs', false, true, false, false);
$channel->queue_declare('all-logs', false, true, false, false);

//队列绑定到交换器
$channel->queue_bind('msg-inbox-errors', 'logs-exchange', 'error.msg-inbox');
$channel->queue_bind('msg-inbox-logs', 'logs-exchange', '*.msg-inbox');
