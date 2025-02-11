from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=400)
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.done == True:
            return self.task + " - Done"
        else:
            return self.task + " - Unfinished"