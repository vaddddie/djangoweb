from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index.as_view(), name='home'),
    path('mode', views.mode.as_view(), name='mode'),
    path('management', views.management, name='management'),
    path('ArinaBeLike', views.ArinaBeLike, name='ArinaBeLike')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)