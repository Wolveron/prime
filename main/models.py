from django.db import models

# Create your models here.

class news(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	# image = models.ImageField()
	date = models.DateField(auto_now_add=True)

def news_add(new_title,new_content):
	new = news()
	new.title = new_title
	new.content = new_content
	new.save()

class mails(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	context = models.TextField()

class product(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	members = models.TextField()
	# image = models.ImageField()
	price = models.IntegerField()
