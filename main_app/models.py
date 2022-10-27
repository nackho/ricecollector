from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.
class Rice(models.Model):
    name = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    usage = models.TextField(max_length=250)

class Picked(models.Model):
    date = models.DateField()

    cat = models.ForeignKey(Rice, on_delete=models.CASCADE)

    def __str__(self):
        return f"Obtained the grain on {self.date}."

    def __str__(self):
        return self.name
 
    def get_absolute_url(self):
        return reverse('detail', kwargs={'rice_id': self.id})