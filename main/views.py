from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, JsonResponse
from .models import *
# Create your views here.

def main(request):
	News = New.objects.all()
	return render(request, 'main.html', {"News" : News})

def catalog(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()

	Products = Product.objects.all().order_by('product_type')
	Types = []
	for some in Products:
		if some.product_type in Types:
			pass
		else:
			Types.append(some.product_type)
	return render(request, 'catalog.html', {"Products" : Products, "Types" : Types})

def bag(request):
	return render(request, 'bag.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	if request.method != "POST":
		return render(request, 'contact.html')
	else:
		mail = Mail(
			name=request.POST.get("name"),
			email=request.POST.get("email"),
			context=request.POST.get("context"))
		mail.save()
		return render(request, 'thanks.html', {"Name" : request.POST.get("name")})

def addcart(request):
	return_dict = dict()
	data = request.POST
	order = Cart()
	order.session_key  = data.get('session_key')
	order.product  = data.get('product_name')
	order.count  = data.get('product_count')
	order.total_price  = int(data.get('product_price'))*int(order.count)
	order.save()
	
	return JsonResponse(return_dict)
