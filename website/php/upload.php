<?php
	//$allowed contains all allowed file types.
	function upload($class, $assignment){
		$target_dir = "/var/www/html/" . $class ."/". $assignment . "/";
		$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
		$extenType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
		if($extenType == "txt"){
			if(move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)){
				echo "The file " . basename($_FILES["fileToUpload"]["name"]). " has been uploaded.";
			}else{
				echo "Sorry, there was an error during upload. Please try again.";
			}
		}
	}
	function addClass($class){
		$target_dir = "/var/www/" . $class;
		mkdir($target_dir);
	}
	function addAssignment($class, $assignment){
		$target_dir = "/var/www/" . $class . "/" . $assignment;
		mkdir($target_dir);
	}
	if(isset($_POST['action']) && !empty($_POST['action'])){
		$action = $_POST['action'];
		switch($action){
			case 'upload' : 
		}
	
	}
?>
