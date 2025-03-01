from django.db import models

class authorModel(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=10)
    Email = models.EmailField()
    phn_number = models.CharField(max_length=12)  
    Instrument_type = models.CharField(max_length=20) 

    def __str__(self):
        return f"{self.First_name} {self.Last_name}"
