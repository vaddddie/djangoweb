from django.shortcuts import render, redirect
from .models import Status, Mode
from .forms import ModeForm
from django.views.generic import ListView, CreateView
from .mqttController import connect_mqtt, output_msg
from datetime import datetime, timedelta, time, date


broker = "192.168.4.1"
port = 1883
topic = "test/blink"
client_id = f"python-mqtt-{0}"


client = connect_mqtt(broker, port, topic, client_id)
client.loop_start()



class index(ListView):
    model = Status
    template_name = 'main/index.html'
    context_object_name = 'statuses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        statuses = Status.objects.all()
        for status in statuses:

            if status.Working:
                temp = int((status.TimeTarget - datetime.now()).total_seconds())

                if temp > 0:
                    seconds = temp

                    days, seconds = divmod(seconds, 86400)
                    hours, seconds = divmod(seconds, 3600)
                    minutes, seconds = divmod(seconds, 60)

                    if int(hours) < 10:
                        hours = '0' + f'{hours}'

                    if int(minutes) < 10:
                        minutes = '0' + f'{minutes}'

                    if int(seconds) < 10:
                        seconds = '0' + f'{seconds}'

                else:
                    days = 0
                    hours = minutes = seconds = '00'

                suffix = ''
                if days > 1 or days == 0:
                    suffix = 's'

                status.TimeLeft = f'{days} day{suffix} {hours}:{minutes}:{seconds}'

                ABSTime = 1000000

                if temp > 0:
                    status.GrowthProcess = (ABSTime - temp) / ABSTime
                else:
                    status.GrowthProcess = 100

            if abs(datetime.now() - status.TimeDelta) > timedelta(0, 15):
                status.CheckLine = False
            else:
                status.CheckLine = True
            status.save()
        return context


def management(request):
    statuses = Status.objects.all()
    mods = Mode.objects.all()
    for status in statuses:
        i = status.id
        if request.POST.get(f"NameSend{i}") and request.POST.get(f"ChangeName{i}") != '':
            status.FarmName = request.POST.get(f"ChangeName{i}")
            status.save()
            return redirect('/management')

        if request.POST.get(f"CoolerOn{i}"):
            msg = {
                "MAC": status.MacAddress,
                "state": 1
            }
            output_msg(client, msg, 'test/cooler')

        if request.POST.get(f"CoolerOff{i}"):
            msg = {
                "MAC": status.MacAddress,
                "state": 2
            }
            output_msg(client, msg, 'test/cooler')

        if request.POST.get(f"WateringOn{i}"):
            msg = {
                "MAC": status.MacAddress,
                "state": 1
            }
            output_msg(client, msg, 'test/pump')
        if request.POST.get(f"WateringOff{i}"):
            msg = {
                "MAC": status.MacAddress,
                "state": 2
            }
            output_msg(client, msg, 'test/pump')

        if request.POST.get(f"LightOn{i}"):
            msg = {
                "MAC":status.MacAddress,
                "state":1
            }
            output_msg(client, msg, 'test/light')
            pass
        if request.POST.get(f"LightOff{i}"):
            msg = {
                "MAC": status.MacAddress,
                "state": 2
            }
            output_msg(client, msg, 'test/light')
            pass

        if request.POST.get(f"Default{i}"):
            msg = {
                "MAC": status.MacAddress,
                "state": 0
            }
            output_msg(client, msg, 'test/light')
            output_msg(client, msg, 'test/pump')
            output_msg(client, msg, 'test/cooler')

        if request.POST.get(f"Stop{i}"):
            status.Working = False
            status.GrowthProcess = 0
            status.save()

        if request.POST.get(f'Again{i}'):
            status.TimeTarget = datetime.now() + timedelta(14)
            status.save()

        if request.POST.get(f"Accept{i}") and request.POST.get('ModsSelect') is not None:
            temp = request.POST.get('ModsSelect')
            status.Mode = temp
            status.Working = True
            status.TimeTarget = datetime.now() + timedelta(14)
            status.save()
            modes = Mode.objects.get(ModName=temp)
            j_string = {
                "ID": status.MacAddress,
                "IWater": modes.IWater,
                "TWater": modes.TWater,
                "ILight": modes.ILight,
                "TLight": modes.TWater,
                "Temperature": modes.Temperature,
                "Humidity": modes.Humidity
            }
            output_msg(client, j_string, 'test/mode')

        if request.POST.get(f'Delete{i}'):
            print('yes')
            status.delete()
            return redirect('/management')

    contex = {
        "statuses": statuses,
        "mods": mods
    }
    return render(request, "main/management.html", contex)


def ArinaBeLike(request):
    statuses = Status.objects.all()
    contex = {
        "statuses": statuses,
    }
    return render(request, "main/ArinaBeLike.html", contex)

"""
def mode(request):
    statuses = Status.objects.all()
    contex = {
        "statuses": statuses,
    }
    return render(request, 'main/mode.html')
"""
class mode(CreateView):
    form_class = ModeForm
    template_name = 'main/mode.html'
    success_url = '/mode'

    def get_contex_date(self, *, object_list=None, **kwargs):
        context = super().get_context_date(**kwargs)
        return context
