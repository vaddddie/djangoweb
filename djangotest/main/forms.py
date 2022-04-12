from django.forms import ModelForm, TextInput
from .models import Status


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


