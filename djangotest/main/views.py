from django.shortcuts import render, redirect
from .models import Status, Mode
from .forms import ModeForm
from django.views.generic import ListView, CreateView, UpdateView
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

            try:
                mode = Mode.objects.get(ModeName=status.Mode)
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

                ABSTime = mode.GrowingTime.total_seconds()

                if temp > 0:
                    status.GrowthProcess = (1 - temp / ABSTime) * 100
                else:
                    status.GrowthProcess = 100

            except Mode.DoesNotExist:
                    status.GrowthProcess = 0
                    status.TimeLeft = 'None'

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
                "state": 1
            }
            output_msg(client, msg, 'test/light')
        if request.POST.get(f"LightOff{i}"):
            msg = {
                "MAC": status.MacAddress,
                "state": 2
            }
            output_msg(client, msg, 'test/light')

        if request.POST.get(f"Default{i}"):
            msg = {
                "MAC": status.MacAddress,
                "state": 0
            }
            output_msg(client, msg, 'test/light')
            output_msg(client, msg, 'test/pump')
            output_msg(client, msg, 'test/cooler')

        if request.POST.get(f'Again{i}'):
            temp = Mode.objects.get(ModeName=status.Mode)
            status.TimeTarget = datetime.now() + temp.GrowingTime
            status.save()

        if request.POST.get(f"Accept{i}") and request.POST.get('ModsSelect') is not None:
            temp = request.POST.get('ModsSelect')
            modes = Mode.objects.get(ModeName=temp)
            status.Mode = temp
            status.TimeTarget = datetime.now() + modes.GrowingTime
            status.save()
            j_string = {
                "ID": status.MacAddress,
                "IWater": int(modes.IWater.total_seconds() * 1000),
                "TWater": int(modes.TWater.total_seconds() * 1000),
                "ILight": int(modes.ILight.total_seconds() * 1000),
                "TLight": int(modes.TLight.total_seconds() * 1000),
                "Temperature": modes.Temperature,
                "Humidity": modes.Humidity
            }
            output_msg(client, j_string, 'test/mode')

        if request.POST.get(f'Delete{i}'):
            status.delete()
            return redirect('/management')

        if request.POST.get(f'sendjson{i}'):
            msg = request.POST.get(f"json{i}")
            topic = request.POST.get(f"topic{i}")
            output_msg(client, msg, topic)

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


class cmode(CreateView):
    form_class = ModeForm
    template_name = 'main/createmodes.html'
    success_url = '/modes'

    def get_contex_date(self, *, object_list=None, **kwargs):
        context = super().get_context_date(**kwargs)
        return context


class modes(ListView):
    model = Mode
    template_name = 'main/mode.html'
    context_object_name = 'mode'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class umodes(UpdateView):
    model = Mode
    form_class = ModeForm
    template_name = 'main/updatemodes.html'
    success_url = '/modes'

    def post(self, request, *args, **kwargs):
        if request.POST.get('Delete'):
            return redirect('/modes')
