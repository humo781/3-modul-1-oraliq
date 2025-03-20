from rest_framework import serializers
from .models import Forecast
from location.serializers import BaseLocationSerializer
from location.models import Location

class ForecastSerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())

    class Meta:
        model = Forecast
        fields = ['id', 'location', 'forecast_date', 'temperature_min', 'temperature_max', 'humidity',
                  'precipitation_probability', 'wind_speed', 'wind_direction', 'created_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['location'] = BaseLocationSerializer(instance.location).data
        return data


class ForecastLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ['id', 'forecast_date', 'temperature_min', 'temperature_max', 'humidity',
                  'precipitation_probability', 'wind_speed', 'wind_direction', 'created_at']
