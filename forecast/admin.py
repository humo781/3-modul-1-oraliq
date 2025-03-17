from django.contrib import admin
from .models import Forecast

@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'forecast_date', 'temperature_min', 'temperature_max', 'created_at')
    list_filter = ('location', 'created_at')
