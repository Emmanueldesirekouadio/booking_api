from django.db import models

from base.helpers.date_time_model import DateTimeModel
from booking.models.providers_model import ProviderModel


class ServiceModel(DateTimeModel):
    provider = models.ForeignKey(ProviderModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()


    def __str__(self):
        return self.name