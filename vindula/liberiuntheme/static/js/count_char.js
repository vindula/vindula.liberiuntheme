$j = jQuery.noConflict();

function countChar(val, max){
     var len = val.value.length;
     if (len >= max) {
              val.value = val.value.substring(0, max);
     } else {
              //$('#charNum').text(max - len);
     }
};

$j(document).ready(function(){
	
	$j('textarea#form-widgets-description_profile').keyup(function(event) {
		countChar($j(this)[0],280);
	})
	
})