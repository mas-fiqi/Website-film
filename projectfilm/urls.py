from django.contrib import admin
from django.urls import include, path
from nontonkuy.views import *

urlpatterns = [
    path('index', index, name='index'),
    path('', login, name='login'),
    path('admin/', admin.site.urls),
]

