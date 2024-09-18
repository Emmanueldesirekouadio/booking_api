# service serializer
from rest_framework import serializers
from booking.models.services_model import ServiceModel


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = '__all__'