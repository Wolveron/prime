from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .forms import *
from .models import *
# Create your views here.

def deff(request):
	return HttpResponsePermanentRedirect('/main.html')

def main(request):
	News = news.objects.all()
	return render(request, 'main.html', {"News" : News})

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

def admin(request):
	if request.method != "POST":
		return render(request, 'admin.html', {"title":"Данный раздел предназначен для персонала"})
	else:
		login = request.POST.get("login")
		password = request.POST.get("password")
		if login == "Свои" and password == "Те же":
			return HttpResponsePermanentRedirect('panel.html')
		else:
			return render(request, 'admin.html', {"title":"Попробуйте ещё раз"})

def panel(request):
	if request.method != "POST":
		return render(request, 'panel.html', {"Title":"Есть чем поделиться?"})
	else:
		if request.POST.get("Delete-btn") == "Delete":
			news.objects.all().delete()
			return render(request, 'panel.html', {"Title":"Очищено"})
		else:
			news_add(request.POST.get("TitleNews"), request.POST.get("ContentNews"), request.POST.get("ImageNews"))
			return render(request, 'panel.html', {"Title":"Продолжим?"})

def testpage(request):
	News = news.objects.all()
	return render(request, 'testpage.html', {"News" : News})