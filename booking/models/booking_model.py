from django.db import models

from base.helpers.date_time_model import DateTimeModel
from booking.models.providers_model import ProviderModel
from booking.models.services_model import ServiceModel


class BookingModel(DateTimeModel):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    provider = models.ForeignKey('ProviderModel', on_delete=models.CASCADE,  related_name='services')
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'La reservation pour {self.customer_name} a été effectué le {self.created_at}'
