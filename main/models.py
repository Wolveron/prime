from django.db import models

# Create your models here.

class New(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	image = models.FileField(default='img/main_logo.jpg')
	date = models.DateField(auto_now_add=True)

class Mail(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	context = models.TextField()

class Product(models.Model):
	product_type = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	description = models.TextField()
	members = models.TextField()
	image = models.FileField(default='img/main_logo.jpg')
	price = models.IntegerField()
	popularity = models.IntegerField(default=0)

class Cart(models.Model):
	session_key = models.CharField(max_length=150)
	product_id = models.ForeignKey(Product, on_delete = models.CASCADE, default=None)
	count = models.IntegerField(default=0)
	total_price = models.DecimalField(decimal_places=2, max_digits=3)