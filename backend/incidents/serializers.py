from rest_framework import serializers
from .models import Personnel, Incident


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Personnel
        fields = ['id', 'slot', 'name', 'color_class']


class IncidentSerializer(serializers.ModelSerializer):
    date   = serializers.DateField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'])
    damage = serializers.DecimalField(max_digits=14, decimal_places=2, coerce_to_string=False)

    class Meta:
        model  = Incident
        fields = [
            'id', 'time', 'date', 'location', 'involved',
            'occupancy', 'damage', 'injured', 'casualty',
            'station', 'engine', 'alarm', 'inputter',
        ]