from django.contrib import admin

# Register your models here.
from places.models import Place, PlaceImage


@admin.register(Place, PlaceImage)
class PlaceAdmin(admin.ModelAdmin):
    pass