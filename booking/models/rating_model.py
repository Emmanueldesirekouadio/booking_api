from django.db import models
from booking.models.services_model import ServiceModel
from base.helpers.date_time_model import DateTimeModel




RATING_CHOICE = [
    (1, 'very bad'),
    (2, 'bad'),
    (3, 'average'),
    (4, 'good'),
    (5, 'excellent')
]

class RatingModel(DateTimeModel):
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, related_name='ratings')
    prestataire = models.ForeignKey('ProviderModel', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.service} - {self.rating}'
