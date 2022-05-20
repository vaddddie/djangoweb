from django.forms import ModelForm, TextInput, DateTimeInput
from .models import Status, Mode

"""
class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ["FarmName"]
        widgets = {
            "FarmName": TextInput(attrs={
                'class': 'form-control',
                'style': 'width:100%'
            })
        }
"""
class ModeForm(ModelForm):
    class Meta:
        model = Mode
        fields = [
            "ModeName",
            "IWater",
            "TWater",
            "ILight",
            "TLight",
            "Temperature",
            "Humidity",
            "GrowingTime"
        ]
        widgets = {
            "ModeName" : TextInput(attrs={
                'class': 'form-control',
                'style': 'height:30px',
                'placeholder': 'Enter a new name'
            }),
            "IWater": DateTimeInput(attrs={
                'class': 'form-control',
                'style': 'height:30px'
            }),
            "TWater": DateTimeInput(attrs={
                'class': 'form-control',
                'style': 'height:30px'
            }),
            "ILight": DateTimeInput(attrs={
                'class': 'form-control',
                'style': 'height:30px'

            }),
            "TLight": DateTimeInput(attrs={
                'class': 'form-control',
                'style': 'height:30px'
            }),
            "Temperature": TextInput(attrs={
                'class': 'form-control',
                'style': 'height:30px',
                'placeholder': 'Enter a temperature'
            }),
            "Humidity": TextInput(attrs={
                'class': 'form-control',
                'style': 'height:30px',
                'placeholder': 'Enter a humidity'
            }),
            "GrowingTime": DateTimeInput(attrs={
                'class': 'form-control',
                'style': 'height:30px'
            }),
        }



