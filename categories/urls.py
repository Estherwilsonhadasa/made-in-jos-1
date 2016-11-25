from django.conf.urls import url, include
from . views import (
	jay
	)

urlpatterns = [
	url(r'cat/$', jay),
	
]

