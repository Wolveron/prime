from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, JsonResponse
from .models import *
from itertools import chain
# Create your views here.

def basePrime(request):
	return render(request, 'base_prime.html')



def main(request):
	cart = orderSize(request)
	News = New.objects.all()
	return render(request, 'main.html', {"News" : News, "Cart" : cart,})

def catalog(request):
	cart = orderSize(request)
	full = Product.objects.all().order_by('product_type')
	if request.method == "POST" and request.POST.get("search") != "":
		q = request.POST.get("search")
		Products = []
		for item in full:
			if q in item.name or q in item.members or q in item.description or q in item.product_type:
				Products.append(item)
	else:
		Products = full
	Types = []
	for some in Products:
		if some.product_type in Types:
			pass
		else:
			Types.append(some.product_type)
	return render(request, 'catalog.html', {"Products" : Products, "Types" : Types, "Cart" : cart,})

def bag(request):
	session_key = request.session.session_key
	cart = orderSize(request)
	sales = Cart.objects.filter(session_key=session_key)
	total = 0
	for item in sales:
		total = total + item.total_price 
	return render(request, 'bag.html', {"Cart" : cart, "Sales" : sales, "Total" : total})

def about(request):
	cart = orderSize(request)
	return render(request, 'about.html', {"Cart" : cart,})

def contact(request):
	cart = orderSize(request)
	if request.method != "POST":
		return render(request, 'contact.html', {"Cart" : cart,})
	else:
		mail = Mail(
			name=request.POST.get("name"),
			email=request.POST.get("email"),
			context=request.POST.get("context"))
		mail.save()
		text = "Благодарим за Ваш отзыв, " + request.POST.get('name') + "! "
		return render(request, 'thanks.html', {"Text" : text, "Cart" : cart,})

def orderCreate(request):
	if request.method != "POST":
		return HttpResponsePermanentRedirect('main.html')
	else:
		cart = orderSize(request)
		session_key = request.session.session_key
		basket = Cart.objects.filter(session_key=session_key)
		order = Order(order_list="Заказ:")
		for item in basket:
			order.order_list = order.order_list + '\n' + item.product.name + " " + str(item.count) + " шт. на сумму: " + str(item.total_price)
			order.total += item.total_price
		order.address = request.POST.get("address")
		order.contact = request.POST.get("contact")
		order.save()
		basket.delete()
		text = "Благодарим за Ваш заказ! В ближайшее время с Ваши свяжется наш оператор для подтверждения заказа. "
		return render(request, 'thanks.html', {"Text" : text, "Cart" : cart,})		

def addcart(request):
	data = request.POST
	session_key = request.session.session_key
	name = data.get('product_name')
	product = Product.objects.get(name=name)
	order, created = Cart.objects.get_or_create(session_key=session_key, product=product)
	order.count += int(data.get('product_count'))
	order.total_price  = int(data.get('product_price')) * int(order.count)
	order.save()
	cart_size = {}
	cart_size['total_order'] = orderSize(request)
	return JsonResponse(cart_size)

def saleremove(request):
	data = request.POST
	session_key = request.session.session_key
	name = data.get('name')
	count = data.get('count')
	product = Product.objects.get(name=name)
	sales = Cart.objects.filter(session_key=session_key)
	total = 0
	for item in sales:
		if item.product == product:
			new_count = int(item.count) - int(count)
			new_total_price = int(product.price) * new_count
			if new_count <= 0:
				item.delete()
			else:
				item.count = new_count
				item.total_price = new_total_price
				item.save()
				total = total + item.total_price
		else:		
			total = total + item.total_price 
	cart_size = {}
	cart_size['total_order'] = orderSize(request)
	cart_size['new_total_price'] = new_total_price
	cart_size['new_count'] = new_count
	cart_size['total'] = total
	return JsonResponse(cart_size)


def orderSize(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	order = Cart.objects.filter(session_key=session_key)
	cart = 0
	for item in order:
		cart += item.count
	return cart