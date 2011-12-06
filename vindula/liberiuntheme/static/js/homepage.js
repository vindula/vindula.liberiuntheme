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
	
	
	
	/* START GALLERY CYCLE AND HEIGHT CONTENT BOXES */
	
	var height = $j('#info-destaque-1').height();
	var max_height = height;
	for(var i=1; i <= document.querySelectorAll("#content-boxes").length; i++)
	{
		$j('#cont-boxes-'+i).cycle({
			fx: 'fade',
			speed: 500,
			timeout: 0,
			next: '#cycle-next-boxes-'+i,
			prev: '#cycle-prev-boxes-'+i,
			pager:'#cycle-nav-boxes-'+i,
		});
		
	    for(var n=1; n <= $j('div#cont-boxes-'+i+' div.info_destaque').length; n++)
	    {
	        height = $j('div#cont-boxes-'+i+' div#info-destaque-'+n).height()
	        if(height > max_height)
	        {
	            max_height = height;
	        }
	    }
	}
	
	$j('#cont-boxes-1').height(max_height+10);
	
	$j(window).resize(function() {
        var height = $j('#info-destaque-1').height();
	    var max_height = height;
	
	    for(var i=1; i <= document.querySelectorAll("#content-boxes").length; i++)
	    {
	        for(var n=1; n <= $j('div#cont-boxes-'+i+' div.info_destaque').length; n++)
	        {
	            height = $j('div#cont-boxes-'+i+' div#info-destaque-'+n).height()
	            if(height > max_height)
	            {
	                max_height = height;
	            }
	        }
	    }
	    
	    $j('#cont-boxes-1').height(max_height+10);
	});
	
	/* END GALLERY CYCLE AND HEIGHT CONTENT BOXES */
	
});