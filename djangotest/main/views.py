from django.shortcuts import render, redirect
from .models import Status


def index(request):
    statuses = Status.objects.all()
    return render(request, 'main/index.html', {'statuses': statuses})


def management(request):
    statuses = Status.objects.all()
    if request.POST.get('TempSet'):
        print("Кнопка сет")
        print("no")
    if request.POST.get('LightOn'):
        print("СЮДАААА ЛУУУУТ")
    if request.POST.get('LightOff'):
        print("СЮДАААА ЛУУУУТ")
    if request.POST.get('WateringOn'):
        print("СЮДАААА ЛУУУУТ")
    if request.POST.get('WateringOff'):
        print("СЮДАААА ЛУУУУТ")
    if request.POST.get('Default'):
        print("СЮДАААА ЛУУУУТ")
    return render(request, 'main/management.html', {'statuses': statuses})


def mode(request):
    return render(request, 'main/mode.html')
