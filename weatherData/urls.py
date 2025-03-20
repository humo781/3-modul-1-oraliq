from django.urls import path
from . import views

urlpatterns = [
    path('weather-data/', views.WeatherDataApiView.as_view(), name='create-list'),
    path('weather-data/<int:pk>/', views.WeatherDataDetailApiView.as_view(), name='detail'),
    path('weather-data/location/<int:pk>/', views.WeatherDataLocationDetailApiView.as_view(), name='location-detail'),
]
