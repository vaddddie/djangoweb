from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('management', views.management, name='management'),
    path('mode', views.mode, name='mode')
]