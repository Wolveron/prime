$(document).ready(function(){
	$('.btn-cart-add').click(function(e){
		e.preventDefault();
		form = $(this).parents('form');
		input = form.find('.count-cart-add');
		var product_name = $(this).data('name');
		var product_price = $(this).data('price');
		var product_count = input.val();
		var token = form.children(input).val();
		data = {};
		data.product_name = product_name;
		data.product_count = product_count;
		data.product_price = product_price;
		data['csrfmiddlewaretoken'] = token;
		var url = form.attr('action');
		$.ajax({
			url : url,
			type : 'POST',
			data : data,
			cache : true,
			success : function(data){
				console.log('OK');
				$('#cart-size').text('('+data.total_order+')');
			},
			error: function(){
				console.log('Wrong');
			},
		});
		console.log('End');
	}),
	$('.btn-sale-remove').click(function(e){
		e.preventDefault();
		var name = $(this).data('name');
		var token = $(this).parents('div').children('input').val();
		var main = $(this).parents('.sale-item')
		console.log(name);
		data = {};
		data.name = name;
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
