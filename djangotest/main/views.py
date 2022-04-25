from django.shortcuts import render, redirect
from .models import Status
# from .forms import StatusForm
from django.views.generic import ListView
from .mqttController import connect_mqtt, blink
from datetime import datetime, timedelta


broker = "192.168.4.1"
port = 1883
topic = "test/blink"
client_id = f"python-mqtt-{0}"


client = connect_mqtt(broker, port, topic, client_id)
client.loop_start()



class index(ListView):
    model = Status
    template_name = 'main/index.html'
    for i in range(1, len(statuses) + 1):
        status = Status.objects.get(id=i)
        if abs(datetime.now() - status.TimeDelta) > datetime(0, 0, 0, 0, 0, 15):
            status.CheckLine = False
        else:
            status.CheckLine = True
        status.save()
    context_object_name = 'statuses'
"""
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
"""
"""
class management(ListView):
    model = Status
    template_name = 'main/management.html'
    context_object_name = 'statuses'
    # form_class = StatusForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'] = StatusForm()
        return context
"""


def management(request):
    statuses = Status.objects.all()
    for i in range(1, len(statuses) + 1):
        if request.POST.get(f"NameSend{i}"):
            status = Status.objects.get(id=i)
            status.FarmName = request.POST.get(f"ChangeName{i}")
            status.save()
            return redirect('/management')

        if request.POST.get(f"CoolerOn{i}"):
            pass
            #print(LightOn.auto_id)
            #blink(client, 1, topic)
        if request.POST.get(f"CoolerOff{i}"):
            pass
            #blink(client, 0, topic)

        if request.POST.get(f"WateringOn{i}"):
            pass
            #blink(client, 1, topic)
        if request.POST.get(f"WateringOff{i}"):
            pass
            #blink(client, 0, topic)

        if request.POST.get(f"LightOn{i}"):
            pass
            # blink(client, 1, topic)
        if request.POST.get(f"LightOff{i}"):
            pass
            # blink(client, 0, topic)

        if request.POST.get(f"Default{i}"):
            pass
            #blink(client, 0, topic)
    contex = {
        "statuses": statuses
    }
    return render(request, "main/management.html", contex)


def mode(request):
    return render(request, "main/mode.html")
