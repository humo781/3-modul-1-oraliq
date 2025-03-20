from django.db.models import Avg, Sum, Max
from rest_framework.response import Response
from rest_framework.views import APIView

from weatherData.models import WeatherData


class TemperatureAverageApiView(APIView):
    def get(self, request):
        avg_temp = WeatherData.objects.aggregate(avg_temp=Avg('temperature'))['avg_temp']
        return Response({'average_temperature': round(avg_temp, 2)} if avg_temp is not None else 0)

class PrecipitationSumApiView(APIView):
    def get(self, request):
        precipitation_sum = WeatherData.objects.aggregate(precipitation_sum=Sum('precipitation'))['precipitation_sum']
        return Response({'total_precipitation': round(precipitation_sum, 1)} if precipitation_sum is not None else 0)

class WindSpeedMaxApiView(APIView):
    def get(self, request):
        wind_speed_max = WeatherData.objects.aggregate(wind_speed_max=Max('wind_speed'))['wind_speed_max']
        return Response({"max_wind_speed": round(wind_speed_max, 2)} if wind_speed_max is not None else 0)
