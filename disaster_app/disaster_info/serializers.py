from rest_framework import serializers
from .models import Disaster, Location, Alert

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class DisasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disaster
        fields = "__all__"

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = "__all__"
