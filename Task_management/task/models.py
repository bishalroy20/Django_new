from django.db import models
from category.models import add_category
# Create your models here.

class addtask(models.Model):
    tasktitle = models.CharField(max_length=100)
    taskdescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_Date = models.DateField()
    categories = models.ManyToManyField(add_category )

    def __str__(self):
        return self.tasktitle

