from django.urls import path
from . import views

urlpatterns = [
    path('location/', views.LocationApiView.as_view(), name='list-create'),
    path('location/<int:pk>/', views.LocationDetailApiView.as_view(), name='detail'),
]
