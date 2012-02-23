$j = jQuery.noConflict();

$j(document).ready(function(){
	
	$j('#formfield-form-widgets-content_list_collection_left').hide();
	$j('#formfield-form-widgets-content_list_collection_right').hide();
	
	$j('#form-widgets-choice_type_left-0').change(function(){
		if ($j('#form-widgets-choice_type_left-0')["0"].checked) {
			$j('#formfield-form-widgets-content_list_left').hide();
			$j('#formfield-form-widgets-content_list_collection_left').show();
		}
		else {
			$j('#formfield-form-widgets-content_list_left').show();
			$j('#formfield-form-widgets-content_list_collection_left').hide();
		}
	});
	
	$j('#form-widgets-choice_type_right-0').change(function(){
		if ($j('#form-widgets-choice_type_right-0')["0"].checked) {
			$j('#formfield-form-widgets-content_list_right').hide();
			$j('#formfield-form-widgets-content_list_collection_right').show();
		}
		else {
			$j('#formfield-form-widgets-content_list_right').show();
			$j('#formfield-form-widgets-content_list_collection_right').hide();
		}
	});
	
});