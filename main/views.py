from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from .forms import *
# Create your views here.

def deff(request):
	return HttpResponsePermanentRedirect('/main.html')

def main(request):
	News = News_Form()
	return render(request, 'main.html', {"News_Form" : News})

def catalog(request):
	return render(request, 'catalog.html')

def bag(request):
	return render(request, 'bag.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')
