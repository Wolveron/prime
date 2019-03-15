from django.contrib import admin

# Register your models here.

from .models import *

class NewAdmin(admin.ModelAdmin):
	list_display = [ field.name for field in New._meta.fields ]

admin.site.register(New, NewAdmin)

class MailAdmin(admin.ModelAdmin):
	list_display = [ field.name for field in Mail._meta.fields ]

admin.site.register(Mail, MailAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = [ field.name for field in Product._meta.fields ]

admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
	list_display = [ field.name for field in Cart._meta.fields ]

admin.site.register(Cart, CartAdmin)

class OrderAdmin(admin.ModelAdmin):
	list_display = [ field.name for field in Order._meta.fields ]

admin.site.register(Order, OrderAdmin)
