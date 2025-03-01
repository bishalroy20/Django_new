from django.db import models
from form_page.models import authorModel
from django.core.validators import MinValueValidator, MaxValueValidator

class Album(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(authorModel, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField(null=True, blank=True)  # Allowing NULL values
    rating = models.IntegerField()

    def __str__(self):
        return self.album_name

