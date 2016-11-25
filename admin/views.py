from django.shortcuts import render 
from django.http import HttpResponse
import datetime

from users.models import Register
from categories.models import Category, Carousel1, Carousel2
from users.forms import UserForm
# Create your views here.
def register(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
	context = {
		'form': form
		}
	return render(request, 'index.html', context)