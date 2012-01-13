$j = jQuery.noConflict();

function changeCell(option){
	
}

function fildChecked(value, type){

	for(var i = 0; i <= $j('input:checked').length; i++){
		id = $j('input:checked').eq(i).attr('id');
		if(id == "1")
			value += 1500;
		if(id == "2")
			value += 100;
		if(type == "professional"){
			if(id == "3")
				value += 200;
		}
	}
	
	return value;
}

$j(document).ready(function(){
	var value_prof = parseInt($j('#grand-tot-prof').attr('value'));
	var value_exec = parseInt($j('#grand-tot-exec').attr('value'));
	
	$j('#servers-professional').change(function(){
		option = $j('#servers-professional option:selected').attr('id');
		if (option == "1") {
			value_prof = 900;
			option_old = $j('#professional .show-cell').attr('id');
			if(option_old == 'price4'){
				value_now = $j('#total #tot-prof #price').show();
				value_now = $j('#total #tot-prof #contact').hide();
			}
			
			$j('#professional span#price1').removeClass('hidden-cell').addClass('show-cell');
			$j('#professional span#price2').removeClass('show-cell').addClass('hidden-cell');
			$j('#professional span#price3').removeClass('show-cell').addClass('hidden-cell');
			$j('#professional span#price4').removeClass('show-cell').addClass('hidden-cell');
			if ($j('input:checked'))
				value_prof = fildChecked(value_prof, "professional")
			
			$j('#grand-tot-prof').attr('value', value_prof);
			$j('#grand-tot-prof').text(value_prof);
		}
		else if (option == "2") {
			value_prof = 1800;
			option_old = $j('#professional .show-cell').attr('id');
			if(option_old == 'price4'){
				value_now = $j('#total #tot-prof #price').show();
				value_now = $j('#total #tot-prof #contact').hide();
			}
			
			$j('#professional span#price1').removeClass('show-cell').addClass('hidden-cell');
			$j('#professional span#price2').removeClass('hidden-cell').addClass('show-cell');
			$j('#professional span#price3').removeClass('show-cell').addClass('hidden-cell');
			$j('#professional span#price4').removeClass('show-cell').addClass('hidden-cell');
			
			if ($j('input:checked'))
				value_prof = fildChecked(value_prof, "professional")
				
			$j('#grand-tot-prof').attr('value', value_prof);
			$j('#grand-tot-prof').text(value_prof);
		}
		else if (option == "3") {
			value_prof = 3300;
			option_old = $j('#professional .show-cell').attr('id');
			if(option_old == 'price4'){
				value_now = $j('#total #tot-prof #price').show();
				value_now = $j('#total #tot-prof #contact').hide();
			}
			
			if ($j('input:checked'))
				value_prof = fildChecked(value_prof, "professional")
			
			$j('#professional span#price1').removeClass('show-cell').addClass('hidden-cell');
			$j('#professional span#price2').removeClass('show-cell').addClass('hidden-cell');
			$j('#professional span#price3').removeClass('hidden-cell').addClass('show-cell');
			$j('#professional span#price4').removeClass('show-cell').addClass('hidden-cell');
			
			$j('#grand-tot-prof').attr('value', value_prof);
			$j('#grand-tot-prof').text(value_prof);
		}
		else if (option == "4") {
			$j('#professional span#price1').removeClass('show-cell').addClass('hidden-cell');
			$j('#professional span#price2').removeClass('show-cell').addClass('hidden-cell');
			$j('#professional span#price3').removeClass('show-cell').addClass('hidden-cell');
			$j('#professional span#price4').removeClass('hidden-cell').addClass('show-cell');
			
			$j('#total #tot-prof #price').hide();
			$j('#total #tot-prof #contact').show();
		}
	})
	
	$j('#servers-executive').change(function(){
		option = $j('#servers-executive option:selected').attr('id');
		if (option == "1") {
			value_exec = 2500;
			option_old = $j('#executive .show-cell').attr('id');
			if(option_old == 'price3'){
				$j('#total #tot-exec #price').show();
				$j('#total #tot-exec #contact').hide();
			}
			
			if ($j('input:checked'))
				value_exec = fildChecked(value_exec, "executive")
					
			$j('#executive span#price1').removeClass('hidden-cell').addClass('show-cell');
			$j('#executive span#price2').removeClass('show-cell').addClass('hidden-cell');
			$j('#executive span#price3').removeClass('show-cell').addClass('hidden-cell');
			
			$j('#grand-tot-exec').attr('value', value_exec);
			$j('#grand-tot-exec').text(value_exec);
		}
		else if (option == "2") {
			value_exec = 5500;
			option_old = $j('#executive .show-cell').attr('id');
			
			if(option_old == 'price3'){
				$j('#total #tot-exec #price').show();
				$j('#total #tot-exec #contact').hide();
			}
			
			if ($j('input:checked'))
				value_exec = fildChecked(value_exec, "executive")

			
			$j('#executive span#price1').removeClass('show-cell').addClass('hidden-cell');
			$j('#executive span#price2').removeClass('hidden-cell').addClass('show-cell');
			$j('#executive span#price3').removeClass('show-cell').addClass('hidden-cell');
			
			$j('#grand-tot-exec').attr('value', value_exec);
			$j('#grand-tot-exec').text(value_exec);
		}
		else if (option == "3") {
			$j('#executive span#price1').removeClass('show-cell').addClass('hidden-cell');
			$j('#executive span#price2').removeClass('show-cell').addClass('hidden-cell');
			$j('#executive span#price3').removeClass('hidden-cell').addClass('show-cell');
			
			$j('#total #tot-exec #price').hide();
			$j('#total #tot-exec #contact').show();
		}
	})
	
	$j('input[type="checkbox"]').change(function(){
		if($j(this).attr('checked')){
			if($j(this).attr('id') == "1"){
				value_exec += 1500;
				value_prof += 1500;
				$j('#grand-tot-exec').attr('value', value_exec);
				$j('#grand-tot-exec').text(value_exec);
				$j('#grand-tot-prof').attr('value', value_prof);
				$j('#grand-tot-prof').text(value_prof);
				$j('tr#first').addClass('selected');
			}
			if($j(this).attr('id') == "2"){
				value_exec += 100;
				value_prof += 100;
				$j('#grand-tot-exec').attr('value', value_exec);
				$j('#grand-tot-exec').text(value_exec);
				$j('#grand-tot-prof').attr('value', value_prof);
				$j('#grand-tot-prof').text(value_prof);
				$j('tr#second').addClass('selected');
			}
			if($j(this).attr('id') == "3"){
				value_prof += 200;
				$j('#grand-tot-prof').attr('value', value_prof);
				$j('#grand-tot-prof').text(value_prof);
				$j('tr#third').addClass('selected');
			}
		}else{
			if($j(this).attr('id') == "1"){
				value_exec -= 1500;
				value_prof -= 1500;
				$j('#grand-tot-exec').attr('value', value_exec);
				$j('#grand-tot-exec').text(value_exec);
				$j('#grand-tot-prof').attr('value', value_prof);
				$j('#grand-tot-prof').text(value_prof);
				$j('tr#first').removeClass('selected');
			}
			if($j(this).attr('id') == "2"){
				value_exec -= 100;
				value_prof -= 100;
				$j('#grand-tot-exec').attr('value', value_exec);
				$j('#grand-tot-exec').text(value_exec);
				$j('#grand-tot-prof').attr('value', value_prof);
				$j('#grand-tot-prof').text(value_prof);
				$j('tr#second').removeClass('selected');
			}
			if($j(this).attr('id') == "3"){
				value_prof -= 200;
				$j('#grand-tot-prof').attr('value', value_prof);
				$j('#grand-tot-prof').text(value_prof);
				$j('tr#third').removeClass('selected');
			}
		}
	});
});