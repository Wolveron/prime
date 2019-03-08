from django.db import models

# Create your models here.

class news(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	image = models.FileField(upload_to='', default='img/main_logo.jpg')
	date = models.DateField(auto_now_add=True)

def news_add(new_title,new_content, new_image):
	new = news()
	new.title = new_title
	new.content = new_content
	new.image = new_image
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

class UploadTest(models.Model):
	file_name = models.CharField(max_length=150)
	file_descriprion = models.TextField()
	file_self = models.FileField(upload_to="", default="img/main_logo.jpg")