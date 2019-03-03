from django.contrib import admin

# Register your models here.
from .models import Spot, Building

admin.site.register(Spot)
admin.site.register(Building)
