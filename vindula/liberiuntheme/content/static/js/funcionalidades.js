$j = jQuery.noConflict();

$j(document).ready(function(){
	//ACCORDION BUTTON ACTION	
	$j('h3.accordionButton').click(function() {
		var item_atual = $j(this);
		var li = item_atual.parent();
		var ul = li.parent();
		var todas_li = li.parent().children();
		var qtd_li = todas_li.length;
		
		for (var i = 0; i < qtd_li; i++) {
			filho = todas_li.eq(i)
			
			id_li = filho.attr('id');
			//ESCONDENDO IMAGENS
			if (filho.hasClass('link_on')) {
				$j('img#' + id_li).removeClass('imagemAccordionOn');
				$j('img#' + id_li).addClass('imagemAccordionOff');
			}
			
			if (filho.hasClass('link_on')) {
				filho.removeClass('link_on');
				filho.addClass('link_off');
			}
		}
		
		if(li.hasClass('link_off')){
			var id_li = li.attr('id');
			li.removeClass('link_off');
			li.addClass('link_on');
			
			//MOSTRANDO IMAGENS
			$j('img#'+id_li).addClass('imagemAccordionOn');
		}
		
		
		ul.find('div.accordionContent').slideUp('normal');
		//$j('ul span.accordionContent').slideUp('normal');
		item_atual.next().slideDown('normal');
	});
	
	$j('a.image_accordion').fancybox();
 
	//Show only the first feature
	var div_accordion = $j('div.conteudo_funcionalidade');
	var item_li, item_img, item_content;
	for(var item in div_accordion.toArray())
	{
		item = div_accordion.eq(item);
		item_li = item.find('li').first();
		item_img = item.find('.image_accordion img').first();
		item_content = item.find('.accordionContent').first();
		item_li.removeClass('link_off');
		item_li.addClass('link_on');
		item_img.removeClass('imagemAccordionOff');
		item_img.addClass('imagemAccordionOn');
		item_content.slideDown('normal');
	}
});