<?php
	//$allowed contains all allowed file types.
	function upload($class, $assignment){
		$target_dir = "/var/www/html/classes/" . $class ."/". $assignment . "/";
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
		$target_dir = "/var/www/classes/" . $class;
		mkdir($target_dir);
	}
	function addAssignment($class, $assignment){
		$target_dir = "/var/www/classes/" . $class . "/" . $assignment;
		mkdir($target_dir);
	}
	function readFolders($target_dir){
		$show_json = json_encode(scandir($target_dir));
		if($show_json != false){
			echo json_encode(scandir($target_dir));
		}else{
			die("json_encode fail: " . json_last_error_msg());
		}
	}
	if(isset($_POST['action']) && !empty($_POST['action'])){
		$action = $_POST['action'];
		switch($action){
			case 'addClass' : addClass($_POST['name']);
			case 'upload' : addClass($_POST['class'], $_POST['assignment']);
			case 'addAssignment' : addAssignment($_POST['classN'], $_POST['assignmentN']);
			
		}
	}
	if(isset($_GET['action']) && !empty($_GET['action'])){
		readFolders($_GET['dirs']);
	}
?>
