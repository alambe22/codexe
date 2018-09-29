<?php
function uploadFile($target){
	//$allowed contains all allowed file types.
	$allowed = array('py');
	$target_dir = "uploads/";
	$target_file = $target_dir . basename($FILES["$target"]["name"]);
	$uploadOk = 1;
	$extenType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
	if(in_array($extenType, $allowed)){
		if(file_exists($target_file){
			unlink($target_file);
		}
		if(move_uploaded_file($_FILES["$target"]["tmp_name"], $target_file)){
			echo "The file " . basename($_FILES["$target"]["name"]). " has been uploaded.";
		}else{
			echo "Sorry, there was an error during upload. Please try again.";
		}
	}
}
?>