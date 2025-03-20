from rest_framework import serializers
from .models import Location

class BaseLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']

class LocationSerializer(BaseLocationSerializer):
    class Meta(BaseLocationSerializer.Meta):
        fields = BaseLocationSerializer.Meta.fields + ['latitude', 'longitude', 'elevation', 'created_at']
