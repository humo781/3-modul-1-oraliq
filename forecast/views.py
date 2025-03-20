from rest_framework import generics
from . import serializers
from .models import Forecast

class ForecastMixin:
    queryset = Forecast.objects.all()
    serializer_class = serializers.ForecastSerializer

class ForecastApiView(ForecastMixin, generics.ListCreateAPIView):
    pass

class ForecastDetailApiView(ForecastMixin, generics.RetrieveUpdateDestroyAPIView):
    pass

class ForecastLocationApiView(generics.ListAPIView):
    queryset = Forecast.objects.all()
    serializer_class = serializers.ForecastLocationSerializer

    def get_queryset(self):
        return super().get_queryset().filter(location__id=self.kwargs['pk'])
