<?php
	//$allowed contains all allowed file types.
	$target_dir = "/var/www/";
	exec("python3 " . $target_dir . "cloneRepo.py " . $target_dir . "githubRepos.txt");
	
?>
