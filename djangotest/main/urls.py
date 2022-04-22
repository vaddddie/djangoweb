from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='home'),
    #path('management', views.management, name='management'),
    path('mode', views.mode, name='mode'),
    path('management', views.management, name='management')
]