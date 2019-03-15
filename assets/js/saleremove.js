$(document).ready(function(){
	$(.'btn-sale-remove').on('click', function(e){
		e.preventDefault();
		var sale = $(this).data('sale');
		var token = $(this).parents('div').children('input').val();
		var main = $(this).parents('.sale-item')
		data = {};
		data.sale = sale;
		data['csrfmiddlewaretoken'] = token;
		var url = $(this).attr('action');
		$.ajax({
			url : url,
			type : 'POST',
			data : data,
			cache : true,
			success : function(data){
				console.log('OK');
				$('#cart-size').text('('+data.total_order+')');
				main.remove();
			},
			error: function(){
				console.log('Wrong');
			},
		});
		console.log('End');
	})	
})