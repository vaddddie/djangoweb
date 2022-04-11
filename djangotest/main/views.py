from django.shortcuts import render, redirect
from .models import Status
from .mqttoutput import blink
#import mqttController


#broker = '192.168.4.1'
#port = 1883
#topic = "test/blink"
#client_id = f'python-mqtt-{0}'


#Led = 0


#client = mqttController.connect_mqtt(broker, port, topic, client_id)
#client.loop_start()


def index(request):
    statuses = Status.objects.all()
    return render(request, 'main/index.html', {'statuses': statuses})


def management(request):
    statuses = Status.objects.all()
    if request.POST.get('TempSet'):
        blink.blinkOn()
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
