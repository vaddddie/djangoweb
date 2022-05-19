from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index.as_view(), name='home'),
    path('createMode', views.cmode.as_view(), name='cmode'),
    path('modes', views.modes.as_view(), name='mode'),
    path('updateMode/<int:pk>', views.umodes.as_view(), name='umode'),
    path('management', views.management, name='management'),
    path('ArinaBeLike', views.ArinaBeLike, name='ArinaBeLike')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)