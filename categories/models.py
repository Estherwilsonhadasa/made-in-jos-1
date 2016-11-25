from django.db import models

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length = 100)
	image = models.ImageField(upload_to = 'categories_image')
	date_added = models.DateField(auto_now = True)
	class Meta:
		verbose_name_plural = 'Categories'
	def __str__(self):
		return '%s, %s, %s ' %(self.title, self.image, self.date_added)

class Carousel1(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'carousel_images')
	price = models.CharField(max_length = 100)
	discount = models.CharField(max_length = 5)
	def __str__(self):
		return '%s, %s, %s, %s' %(self. title, self.image, self.price, self.discount)
	class Meta:
		verbose_name_plural = 'Carousel1'

class Carousel2(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'carousel_images')
	price = models.CharField(max_length = 100)
	discount = models.CharField(max_length = 5)
	def __str__(self):
		return '%s, %s, %s, %s' %(self. title, self.image, self.price, self.discount)
	class Meta:
		verbose_name_plural = 'Carousel2'


class Product(models.Model):
	title = models.CharField(max_length = 200)
	price = models.CharField(max_length = 100 )
	image = models.ImageField(upload_to = 'Products_images')
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	date_added = models.DateField(auto_now = True)
	def __str__(self):
		return '%s, %s, %s, %s, %s' %(self.title, self.image, self.price, self.category, self.date_added)
	class Meta:
		verbose_name_plural = 'Products'
	


