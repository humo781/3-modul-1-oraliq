from django.urls import path
from . import views

urlpatterns = [
    path('temperature-avg/', views.TemperatureAverageApiView.as_view(), name='temperature-avg'),
    path('precipitation-sum/', views.PrecipitationSumApiView.as_view(), name='precipitation-sum'),
    path('wind-speed-max/', views.WindSpeedMaxApiView.as_view(), name='wind-speed-max'),
]
