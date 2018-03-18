<?php

require_once('../php-amqplib/amqp.inc');
require_once('../config/config.php');
$image_id = $argv[1];
$user_id = $argv[1];
$image_path = $argv[1];

$conn = new AMQPConnection(HOST, PORT, USER, PASS, VHOST);
$channel = $conn->channel();
$channel->exchange_declare('upload-pictures', 'fanout', false, true, false);
$metadata = json_encode(array(
	    'image_id' => $image_id,
	    'user_id' => $user_id,
	    'image_path' => $image_path
	    ));
$msg = new AMQPMessage($metadata, 
                array('content_type' => 'application/json',
	                    'delivery_mode' => 2));
$channel->basic_publish($msg, 'upload-pictures');
$channel->close();
$conn->close();
?>
