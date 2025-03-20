from django.urls import path
from . import views

urlpatterns = [
    path('weather-data/', views.WeatherDataApiView.as_view(), name='create-list'),
    path('weather-data/<int:pk>/', views.WeatherDataDetailApiView.as_view(), name='detail'),
    path('weather-data/location/<int:pk>/', views.WeatherDataLocationDetailApiView.as_view(), name='location-detail'),
    path('analytics/temperature-avg/', views.TemperatureAverageApiView.as_view(), name='temperature-avg'),
    path('analytics/precipitation-sum/', views.PrecipitationSumApiView.as_view(), name='precipitation-sum'),
    path('analytics/wind-speed-max/', views.WindSpeedMaxApiView.as_view(), name='wind-speed-max'),
]
