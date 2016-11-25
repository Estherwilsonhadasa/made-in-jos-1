from django.contrib import admin
from .models import Register

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
	list_display = ['username', 'password', 'email', 'phone_number', 'date_joined']
	list_display_links = ['username', 'date_joined']

admin.site.register(Register, RegisterAdmin)
