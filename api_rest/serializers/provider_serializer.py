from rest_framework import serializers
from booking.models.providers_model import ProviderModel


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderModel
        fields = '__all__'