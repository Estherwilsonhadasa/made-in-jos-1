from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Register(models.Model):
	username = models.CharField(max_length=200)
	email = models.EmailField()
	phone_number = models.CharField(max_length=20)
	password = models.CharField(max_length=100)
	date_joined = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	

	class Meta:
		verbose_name_plural = 'Register'
	def __str__(self):
		return '%s %s %s %s %s' %(self.username, self.email, self.phone_number, self.password, self.date_joined)
	
		