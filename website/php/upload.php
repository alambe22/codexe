<?php
	//$allowed contains all allowed file types.
	function upload(){
	$target_dir = "/var/www/html/";
	$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
	$uploadOk = 1;
	$extenType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
	if($extenType == "txt"){
		if(move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)){
			echo "The file " . basename($_FILES["fileToUpload"]["name"]). " has been uploaded.";
			include("../index.html");
		}else{
			echo "Sorry, there was an error during upload. Please try again.";
		}
	}
	}
?>
