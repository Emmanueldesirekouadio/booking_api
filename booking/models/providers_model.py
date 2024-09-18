from django.db import models
from base.helpers.date_time_model import DateTimeModel


class ProviderModel(DateTimeModel):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)


    def __str__(self):
        return f'{self.first_name} - {self.last_name}'