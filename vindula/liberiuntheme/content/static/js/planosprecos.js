$j = jQuery.noConflict();

$j(document).ready(function() {
	
	$j('.rowHead').click(function() {
		$j(this).nextAll('tr[name='+this.id+']').toggle(500);
		var div_seta = $j(this).find('div.seta');
		div_seta.toggleClass('seta-left');
		div_seta.toggleClass('seta-top');
		return false;
	});
	
	$j('.rowHead').each(function(){
		$j(this).nextAll('tr[name='+this.id+']').hide();
	})
	
	var maxHeight = 0;
	$j('.descriptionPlan').each(function() {
		if (this.clientHeight > maxHeight)
			maxHeight = this.clientHeight;
			
	});
	
	$j('.descriptionPlan').each(function() {
		$j(this).height(maxHeight);
	});
	
});