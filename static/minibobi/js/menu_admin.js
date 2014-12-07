$(function(){
	$(".field-category").hide();
	$(".field-page").hide();
	$(".field-url").hide();
	if ($("#id_mtype").val() == '0' ){
		$(".field-category").show();
		$(".field-page").hide();
		$(".field-url").hide();		
	}
	if ($("#id_mtype").val() == '1' ){
		$(".field-page").show();
		$(".field-category").hide();
		$(".field-url").hide();
	}
	if ($("#id_mtype").val() == '2' ){
		$(".field-page").hide();
		$(".field-category").hide();
		$(".field-url").show();		
	}
	$("#id_mtype").change(function(){
		if ($("#id_mtype").val() == '0' ){
			$(".field-category").show();
			$(".field-page").hide();
			$(".field-url").hide();		
		}
		if ($("#id_mtype").val() == '1' ){
			$(".field-page").show();
			$(".field-category").hide();
			$(".field-url").hide();
		}
		if ($("#id_mtype").val() == '2' ){
			$(".field-page").hide();
			$(".field-category").hide();
			$(".field-url").show();		
		}
	});
});