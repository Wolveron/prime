from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .forms import *
# Create your views here.

def deff(request):
	return HttpResponsePermanentRedirect('/main.html')

def main(request):
	return render(request, 'main.html')

def catalog(request):
	return render(request, 'catalog.html')

def bag(request):
	return render(request, 'bag.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	if request.method != "POST":
		return render(request, 'contact.html')
	else:
		name = request.POST.get("name")
		email = request.POST.get("email")
		context = request.POST.get("context")
		return render(request, 'thanks.html', {"Name":name})