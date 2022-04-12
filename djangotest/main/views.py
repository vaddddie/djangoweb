from django.shortcuts import render, redirect
from .models import Status
from .forms import StatusForm
from .mqttController import connect_mqtt, blink


broker = "192.168.4.1"
port = 1883
topic = "test/blink"
client_id = f"python-mqtt-{0}"


client = connect_mqtt(broker, port, topic, client_id)
client.loop_start()


def index(request):
    statuses = Status.objects.all()
    return render(request, "main/index.html", {"statuses": statuses})


def management(request):
    statuses = Status.objects.all()
    if request.POST.get("NameSend"):
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save("FarmName")
            #print(temp.data['FarmName'])
        else:
            pass

    if request.POST.get("CoolerOn"):
        #print(LightOn.auto_id)
        blink(client, 1, topic)
    if request.POST.get("CoolerOff"):
        pass
        blink(client, 0, topic)
    if request.POST.get("LightOn"):
        #print(LightOn.auto_id)
        blink(client, 1, topic)
    if request.POST.get("LightOff"):
        pass
        blink(client, 0, topic)
    if request.POST.get("WateringOn"):
        blink(client, 1, topic)
    if request.POST.get("WateringOff"):
        blink(client, 0, topic)
    if request.POST.get("Default"):
        blink(client, 0, topic)
    form = StatusForm()
    contex = {
        "form": form,
        "statuses": statuses
    }
    return render(request, "main/management.html", contex)


def mode(request):
    return render(request, "main/mode.html")
