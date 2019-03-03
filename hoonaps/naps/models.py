from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name



class Spot(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.CharField(max_length=10)
    type = models.CharField(max_length=100)
    size = models.IntegerField(default=1)
    noise = models.CharField(max_length=7, default='Average')
    pub_date = models.DateTimeField('Date added')
    notes = models.CharField(max_length=500, default='No notes')
    def __str__ (self):
        return self.building.name+' '+self.type+' (Floor '+self.floor+')'
    def was_added_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
