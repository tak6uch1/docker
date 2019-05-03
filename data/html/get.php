<?php
// Accept only from ajax
$request = isset($_SERVER['HTTP_X_REQUESTED_WITH']) ? strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) : '';
if($request !== 'xmlhttprequest') exit;
 
$text = filter_input(INPUT_POST, 'opt');
echo json_encode(['output_text' => "$text"]);
