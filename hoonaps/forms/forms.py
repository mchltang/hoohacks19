from django import forms
from .models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'location_name',
            'location_type',
            'location_description',
            'longtitude',
            'latitude'
        ]