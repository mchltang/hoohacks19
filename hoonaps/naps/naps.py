from django import forms
from .models import Spot

class SpotForm(forms.ModelForm):
    class Meta:
        model = Spot
        fields = {
            'building',
            'noise',
            'floor',
            'type',
            'size',
            'notes',
            'latitude',
            'longtitude',
        }
