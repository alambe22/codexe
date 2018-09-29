<?php
function uploadFile($target){
	//$allowed contains all allowed file types.
	$allowed = array('py');
	$target_dir = "uploads/";
	$target_file = $target_dir . basename($FILES["$target"]["name"]);
	$uploadOk = 1;
	$
}