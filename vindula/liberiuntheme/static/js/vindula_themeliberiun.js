$j = jQuery.noConflict();

$j(document).ready(function(){
	
	/* PERSONAL TOOLS */
	
	setTextPortalPersonaltools();

	function setTextPortalPersonaltools(){
		if ($j('a#user-name').text() != '') {
			var time = new Date();
			time = time.getHours();
			if (time > 17)  var msg = 'Boa noite, ';
			else if (time > 12) var msg = 'Boa tarde, ';
			else var msg = 'Bom dia, ';
			$j('p#hello').text(msg + $j('a#user-name').text() + '.');
		}
	}
	
	
	/* THEME ADJUSTMENTS */
	
	$j('#portal-column-one').attr('class', $j('#portal-column-one').attr('class') + ' bk-column-one');
	$j('#portal-column-two').attr('class', $j('#portal-column-two').attr('class') + ' bk-column-two');
	
	
	/* FORM EDIT ADJUSTMENTS */
	
	$j('div.autocompleteInputWidget span.option label span').text(function(index, text) {
	 	if ($j(this).text() == '(nothing)') $j(this).text('Nada selecionado');
	} )
	
	
	/* LOGO TOP AND FOOTER */
	
	$j('#portal-header').children('a:first').attr("id", "portal-logo");
	$j('#portal-footer').children('a:first').attr("id", "portal-logo");
	

	/* MENU */
	
	$j('#portal-globalnav li').hover(function() {
		$j(this).find('ul').show();
	},function() {
		$j(this).find('ul').hide();
	});

});