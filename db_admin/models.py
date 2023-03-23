from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    type = models.IntegerField(null=True, blank=True)
    quiet = models.BooleanField(null=True, blank=True)
    wifi = models.IntegerField(null=True, blank=True)
    outlet = models.BooleanField(null=True, blank=True)
    class Meta:
        db_table = 'places'

class Img(models.Model):
    path = models.CharField(max_length=100)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    class Meta:
        db_table = 'imgs'
