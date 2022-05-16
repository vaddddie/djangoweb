from django.forms import ModelForm, TextInput
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
            "ModName",
            "IWater",
            "TWater",
            "ILight",
            "TLight",
            "Temperature",
            "Humidity"
        ]
        widgets = {
            "ModName" : TextInput(attrs={
                'class': 'form-control',
                'style': 'height:30px'
            }),
            "IWater": TextInput(attrs={
                'class': 'form-control',
                'style': 'height:30px'
            }),
            "TWater": TextInput(attrs={
                'class': 'form-control',
                'style': 'height:30px'
            }),
            "ILight": TextInput(attrs={
                'class': 'form-control',
                'style': 'height:30px'

            }),
            "TLight": TextInput(attrs={
                'class': 'form-control',
                'style': 'height:30px'
            }),
            "Temperature": TextInput(attrs={
                'class': 'form-control',
                'style': 'height:30px'
            }),
            "Humidity": TextInput(attrs={
                'class': 'form-control',
                'style': 'height:30px'
            })
        }



