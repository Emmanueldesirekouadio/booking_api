from django.db import models
from django.forms import DateTimeField


class BookingModel(DateTimeField):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)


    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
