from rest_framework import serializers
from booking.models.rating_model import RatingModel


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingModel
        fields = '__all__'