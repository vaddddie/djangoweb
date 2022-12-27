from django.shortcuts import render, redirect
# from .forms import ModeForm
from django.views.generic import ListView, CreateView, UpdateView, View
from .mqttController import connect_mqtt
from .methods import *
from .buttons import get_button


broker = "192.168.4.1"
port = 1883
topic = "test/blink"
client_id = f"python-mqtt-{0}"


client = connect_mqtt(broker, port, topic, client_id)
client.loop_start()


class Farms(ListView):
    model = Cell
    context_object_name = 'cells'
    template_name = 'main/farms_beta.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        choose_the_arrow()
        timer()
        return context


class Management(View):
    template_name = 'main/management_beta.html'
    context = {}

    def post(self, request, *args, **kwargs):
        get_button(request, client)
        self.filling_in_the_context()
        return render(request, self.template_name, self.context)

    def get(self, request, *args, **kwargs):
        self.filling_in_the_context()
        timer()
        return render(request, self.template_name, self.context)

    def filling_in_the_context(self):
        self.context['cells'] = Cell.objects.all()
        self.context['modes'] = Mode.objects.all()


class ModeView(ListView):
    model = Mode
    context_object_name = 'modes'
    template_name = 'main/listOfModes_beta.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def debugger(request, *args, **kwargs):
    return render(request, 'main/index_beta.html')
