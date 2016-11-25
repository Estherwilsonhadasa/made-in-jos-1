from django.contrib import admin
from .models import Carousel1, Carousel2, Category, Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'image', 'date_added']
admin.site.register(Category, CategoryAdmin)

class Carousel1Admin(admin.ModelAdmin):
	list_display = ['title', 'image', 'price', 'discount']

admin.site.register(Carousel1,Carousel1Admin)

class Carousel2Admin(admin.ModelAdmin):
	list_display = ['title', 'image', 'discount', 'price']
admin.site.register(Carousel2,Carousel2Admin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['title', 'price', 'category']
admin.site.register(Product, ProductAdmin)