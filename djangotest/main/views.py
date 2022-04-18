from django.shortcuts import render, redirect
from .models import Status
from .forms import StatusForm
from django.views.generic import UpdateView
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


class Management(UpdateView):
    model = Status
    template_name = 'main/management.html'
    context_object_name = 'form'

    form_class = StatusForm



def management(request):
    statuses = Status.objects.all()
    if request.POST.get("NameSend"):
        pass
    if request.POST.get("CoolerOn"):
        pass
        #print(LightOn.auto_id)
        #blink(client, 1, topic)
    if request.POST.get("CoolerOff"):
        pass
        print(statuses)
        #blink(client, 0, topic)
    if request.POST.get("LightOn"):
        blink(client, 1, topic)
    if request.POST.get("LightOff"):
        blink(client, 0, topic)
    if request.POST.get("WateringOn"):
        pass
        #blink(client, 1, topic)
    if request.POST.get("WateringOff"):
        pass
        #blink(client, 0, topic)
    if request.POST.get("Default"):
        pass
        #blink(client, 0, topic)
    form = StatusForm()
    contex = {
        "form": form,
        "statuses": statuses
    }
    return render(request, "main/management.html", contex)



def mode(request):
    return render(request, "main/mode.html")
