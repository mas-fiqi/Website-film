from django.urls import path
from . import views

urlpatterns = [
    path('nontonkuy/', views.nontonkuy, name='nontonkuy'),
]