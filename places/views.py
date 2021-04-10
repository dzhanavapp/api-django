from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .models import Place
from .serializers import PlaceSerializer


class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    http_method_names = ['get']


