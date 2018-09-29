<?php
	//$allowed contains all allowed file types.
	$target_dir = "/var/www/";
	echo `whoami`;
	exec("python3 " . $target_dir . "test.py");
	
?>
