<?php

require_once('../php-amqplib/amqp.inc');
require_once('../config/config.php');
$conn = new AMQPConnection(HOST, PORT, USER, PASS, VHOST);
$channel = $conn->channel();
function add_points_to_user($user_id){
	echo sprintf("Adding points to user: %s\n", $user_id);
}
$channel->exchange_declare('upload-pictures', 'fanout', false, true, false);

$channel->queue_declare('add-user-point', false, true, false, false);

$channel->queue_bind('add-user-point', 'upload-pictures');
$consumer = function($msg){

	if($msg->body == 'quit'){
		$msg->delivery_info['channel']->
			basic_cancel($msg->delivery_info['consumer_tag']);
	}

	$meta = json_decode($msg->body, true);

	add_points_to_user($meta['user_id']);

	$msg->delivery_info['channel']->
		basic_ack($msg->delivery_info['delivery_tag']);
};
$channel->basic_consume($queue,
	$consumer_tag,
	false,
	false,
	false,
	false,
	$consumer);

while(count($channel->callbacks)) {
	$channel->wait();
}
$channel->close();
$conn->close();
?>
