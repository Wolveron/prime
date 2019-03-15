from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, JsonResponse
from .models import *
# Create your views here.

def main(request):
	cart = orderSize(request)
	News = New.objects.all()
	return render(request, 'main.html', {"News" : News, "Cart" : cart,})

def catalog(request):
	cart = orderSize(request)
	Products = Product.objects.all().order_by('product_type')
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
	return render(request, 'bag.html', {"Cart" : cart, "Sales" : sales,})

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
		return render(request, 'thanks.html', {"Name" : request.POST.get("name"), "Cart" : cart,})

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
	product = Product.objects.get(name=name)
	order = Cart.objects.get(session_key=session_key, product=product)
	order.delete()
	cart_size = {}
	cart_size['total_order'] = orderSize(request)
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