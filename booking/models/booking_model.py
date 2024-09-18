from django.db import models
from django.forms import DateTimeField
from base.helpers.date_time_model import DateTimeModel


class BookingModel(DateTimeModel):
    prestataire = models.ForeignKey( 'ProviderModel', on_delete=models.CASCADE)
    service = models.ForeignKey('ServiceModel', on_delete=models.CASCADE, related_name='booking')
    booking_date = models.DateTimeField()
    customer_name = models.CharField(max_length=225)
    custmer_email = models.EmailField()

    def __str__(self):
        return f'{self.service.name} - {self.customer_name}'
