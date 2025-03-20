from rest_framework import generics
from .models import WeatherData
from .serializers import WeatherDataSerializer, WeatherDataLocationSerializer


class WeatherDataMixin:
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

class WeatherDataApiView(WeatherDataMixin, generics.ListCreateAPIView):
    pass

class WeatherDataDetailApiView(WeatherDataMixin, generics.RetrieveUpdateDestroyAPIView):
    pass

class WeatherDataLocationDetailApiView(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataLocationSerializer

    def get_queryset(self):
        return super().get_queryset().filter(location__id=self.kwargs['pk'])
