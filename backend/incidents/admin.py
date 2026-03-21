from django.contrib import admin
from .models import Personnel, Incident

@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ['slot', 'name']

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display  = ['id', 'date', 'time', 'location', 'involved', 'damage', 'inputter']
    list_filter   = ['involved', 'alarm']
    search_fields = ['location', 'station', 'inputter']