from django.db import models


class ParkingLot(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    picture = models.ImageField(upload_to='parking_lot_pictures/')

    def __str__(self):
        return self.name
