from django.db import models
from TaskCategory.models import category
import datetime

# Create your models here.
class taskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField(default=datetime.date.today)
    categories = models.ManyToManyField(category)

    def __str__(self):
        return self.taskTitle

