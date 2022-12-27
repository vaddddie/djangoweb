from django.urls import path
from . import views

urlpatterns = [
    path('', views.Farms.as_view(), name='farms'),
    path('Management', views.Management.as_view(), name='management'),
    path('debugger', views.debugger, name='debugger'),
    path('Modes', views.ModeView.as_view(), name='modes'),
]
