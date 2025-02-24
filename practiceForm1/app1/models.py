from django.db import models

class SModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    # image_field = models.ImageField(upload_to='')
    json_field = models.JSONField()
    # one_to_one_field = models.OneToOneField(name , on_delete=None)
    slug_field = models.SlugField()
    time_field = models.TimeField()
    