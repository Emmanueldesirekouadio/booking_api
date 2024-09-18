from django.db import models
from booking.models.services_model import ServiceModel

RATING_CHOICES = [
    (1, 'very bad'),
    (2, 'bad'),
    (3, 'average'),
    (4, 'good'),
    (5, 'excellent')
]

class RatingModel(models.Model):
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.service} - {self.rating}'
