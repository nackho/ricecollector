from pyexpat import model
from django.db import models

# Create your models here.
class Rice(models.Model):
    name = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    usage = models.TextField(max_length=250)

    def __str__(self):
        return self.name
 