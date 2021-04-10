from rest_framework import serializers

from places.models import Place, PlaceImage


class PlaceImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlaceImage
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    images = PlaceImageSerializer(many=True, read_only=True, source='place_image')

    class Meta:
        model = Place
        fields = ('id', 'name', 'latitude','longitude', 'images')