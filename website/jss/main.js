$(document).ready(function(){
	$("#addAsgn").click(function(){
		console.log("dsaklhflkjdhfklgjhadfklgrf");
	});
});

$(document).ready(function(){
	$("#fileUp").click(function(){
		console.log("zoop");
		var form_data = new FormData(document.getElementById("asgn1"));
		$.ajax({
			url: 'upload.php',
			type: 'POST',
			dataType: 'text',
			cache: false,
			contentType: false,
			processData: false,
			data: form_data,
			success: function(){
				return true;
			}
		});
	});
});