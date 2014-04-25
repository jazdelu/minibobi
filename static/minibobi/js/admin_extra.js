$(function(){
	$(document).ready(function(){
		$(".field-express").css("display","none");
		$(".field-enum").css("display","none");
		if($("#id_status").val() == 'deliver' | $("#id_status").val() == 'complete' ){
			$(".field-express").css("display","table-header-group");
			$(".field-enum").css("display","table-header-group");		
		}	
	});
	$("#id_status").change(function(){
		if($("#id_status").val() == 'deliver' | $("#id_status").val() == 'complete' ){
			$(".field-express").css("display","table-header-group");
			$(".field-enum").css("display","table-header-group");		
		}
		else{
			$(".field-express").css("display","none");
			$(".field-enum").css("display","none");	
		}		
	});
});


