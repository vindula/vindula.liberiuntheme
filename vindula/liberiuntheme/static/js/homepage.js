$j = jQuery.noConflict();

$j(document).ready(function(){

	/* GALLERY CYCLE NEWS */
	
	var cycle_timeout = $j('input#cycle-timeout').attr('value');
	var cycle_height = $j('input#cycle-height').attr('value');
	
	$j('#cont_banner').cycle({
	    fx:     'scrollHorz',
	    speed:   800,
	    timeout: parseInt(cycle_timeout),
	    next:   '#cycle-next',
	    prev:   '#cycle-prev',
		pager:  '#cycle-nav',
		height:	parseInt(cycle_height),
	});
	/*
	var items = $j('#cycle-nav a:last').text();
	var active = $j('#cycle-nav a.activeSlide').text();
	$j('.paginacao p').text(active + '/' + items);
	
	function test(){
		var active = $j('#cycle-nav a.activeSlide').text();
		$j('.paginacao p').text(active + '/' + items);
	}*/
	
	

	
});