from rest_framework import generics
from .serializers import LocationSerializer
from .models import Location

class LocationMixin:
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationApiView(LocationMixin, generics.ListCreateAPIView):
    pass

class LocationDetailApiView(LocationMixin, generics.RetrieveUpdateDestroyAPIView):
    pass
