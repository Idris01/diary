from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass

class Todo(models.Model):
    title=models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        if self.completed:
            comp="Completed"
        else:
            comp="UnCompleted"

        return "{} : {}".format(self.title,comp)

