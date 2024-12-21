from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=200, default="")
    active = models.BooleanField(default=True)

    
def __str__(self):
    return self.name
