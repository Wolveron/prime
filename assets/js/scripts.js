$(document).ready(function(){
	$('.btn-cart-add').on('click', function(e){
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
		console.log(data);
		var url = form.attr('action');
		$.ajax({
			url : url,
			type : 'POST',
			data : data,
			cache : true,
			success : function(data){
				console.log('OK');
				console.log(data);
			},
			error: function(){
				console.log('Wrong');
			},
		});

		console.log('End');
	})

})