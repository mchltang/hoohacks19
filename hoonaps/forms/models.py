from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=200)
    location_type = models.CharField(max_length=200)
    location_description = models.TextField()
    longtitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.location_name + " " + self.location_type