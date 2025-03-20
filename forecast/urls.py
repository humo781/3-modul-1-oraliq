from django.urls import path
from . import views

urlpatterns = [
    path('forecast/', views.ForecastApiView.as_view(), name='list-create'),
    path('forecast/<int:pk>/', views.ForecastDetailApiView.as_view(), name='detail'),
    path('forecast/location/<int:pk>/', views.ForecastLocationApiView.as_view(), name='location-detail'),
]
