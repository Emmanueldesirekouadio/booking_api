from rest_framework import serializers
from booking.models.booking_model import BookingModel


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = '__all__'