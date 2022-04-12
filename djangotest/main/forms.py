from django.forms import ModelForm, TextInput
from .models import Status


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ["Temperature"]
        widgets = {
            "Temperature": TextInput(attrs={
                'class': 'form-control',
                'placeholder': '°C',
                'style': 'width:100%; text-align: right'
            })
        }


