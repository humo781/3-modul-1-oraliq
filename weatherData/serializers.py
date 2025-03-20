from rest_framework import serializers
from .models import WeatherData
from location.serializers import BaseLocationSerializer
from location.models import Location

class WeatherDataSerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())

    class Meta:
        model = WeatherData
        fields = ['id', 'location', 'temperature', 'humidity', 'pressure', 'wind_speed',
                  'wind_direction', 'precipitation', 'recorded_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['location'] = BaseLocationSerializer(instance.location).data
        return data

class WeatherDataLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['id', 'temperature', 'humidity', 'pressure', 'wind_speed',
                  'wind_direction', 'precipitation', 'recorded_at']
