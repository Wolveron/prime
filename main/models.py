from django.db import models

# Create your models here.

class new(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	image = models.FileField(default='img/main_logo.jpg')
	date = models.DateField(auto_now_add=True)

class mail(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	context = models.TextField()

class product(models.Model):
	product_type = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	description = models.TextField()
	members = models.TextField()
	image = models.FileField(default='img/main_logo.jpg')
	price = models.IntegerField()