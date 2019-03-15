from django.db import models

# Create your models here.

class New(models.Model):
	title = models.CharField(max_length=255, verbose_name=u'Заголовок')
	content = models.TextField(verbose_name=u'Содержание')
	image = models.FileField(default='img/logo.jpg', verbose_name=u'Изображение')
	date = models.DateField(auto_now_add=True)
	class Meta:
		verbose_name = u'Новость'
		verbose_name_plural = u'Новости'
	def __str__(self):
		return self.title

class Mail(models.Model):
	name = models.CharField(max_length=255, verbose_name=u'Отправитель')
	email = models.EmailField(verbose_name=u'Обратная связь')
	context = models.TextField(verbose_name=u'Содержание')
	class Meta:
		verbose_name = u'Отзыв'
		verbose_name_plural = u'Отзывы'
	def __str__(self):
		return self.name

class Product(models.Model):
	product_type = models.CharField(max_length=255, verbose_name=u'Тип')
	name = models.CharField(max_length=255, verbose_name=u'Название')
	description = models.TextField(verbose_name=u'Описание')
	members = models.TextField(verbose_name=u'Состав')
	image = models.FileField(default='img/logo.jpg', verbose_name=u'Изображение')
	price = models.IntegerField(verbose_name=u'Цена')
	popularity = models.IntegerField(default=0, verbose_name=u'Популярность')
	class Meta:
		verbose_name = u'Продукт'
		verbose_name_plural = u'Продукты'
	def __str__(self):
		return self.name

class Cart(models.Model):
	session_key = models.CharField(max_length=150, verbose_name=u'Идентификатор')
	product = models.ForeignKey(Product, on_delete = models.CASCADE, default=None, verbose_name=u'Продукт')
	count = models.IntegerField(default=0, verbose_name=u'Количество')
	total_price = models.IntegerField(default=0, verbose_name=u'Общая цена')
	class Meta:
		verbose_name = u'Корзина'
		verbose_name_plural = u'Корзины'