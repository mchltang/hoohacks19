from django.contrib import admin

# Register your models here.
from .models import Spot, Building, Noise

admin.site.register(Spot)
admin.site.register(Building)
admin.site.register(Noise)
