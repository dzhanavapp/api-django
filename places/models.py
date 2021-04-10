from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.name} ({self.id})'


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place_image')
    photo = models.FileField(upload_to='uploads/places/', max_length=254)