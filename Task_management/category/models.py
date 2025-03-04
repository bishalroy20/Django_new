from django.db import models

# Create your models here.
class add_category(models.Model):
    Category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Category_name