from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import *
# Create your views here.

def main(request):
	News = new.objects.all()
	return render(request, 'main.html', {"News" : News})

def catalog(request):
	Products = product.objects.all().order_by('product_type')
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
		mail = mail(
			name=request.POST.get("name"),
			email=request.POST.get("email"),
			context=request.POST.get("context"))
		mail.save()
		return render(request, 'thanks.html', {"Name" : request.POST.get("name")})


