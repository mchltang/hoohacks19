from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Noise(models.Model):
    level = models.CharField(max_length=7)
    def __str__(self):
        return self.level

class Spot(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    noise = models.ForeignKey(Noise, on_delete=models.CASCADE)

    floor = models.CharField(max_length=10)
    type = models.CharField(max_length=100)
    size = models.IntegerField(default=1)
    notes = models.CharField(max_length=500, default='No notes')
    latitude = models.FloatField()
    longtitude =  models.FloatField()
    def __str__ (self):
        return self.building.name+' '+self.type+' (Floor '+self.floor+')'
