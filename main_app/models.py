from pyexpat import model
from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.

class Dish(models.Model):
  name = models.CharField(max_length=50)
  ethnicity = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('dishes_detail', kwargs={'pk': self.id})
    
class Rice(models.Model):
    name = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    usage = models.TextField(max_length=250)
    dishes = models.ManyToManyField(Dish)

    def __str__(self):
        return self.name
 
    def get_absolute_url(self):
        return reverse('detail', kwargs={'rice_id': self.id})

class Picked(models.Model):
    date = models.DateField('Obtained grain')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])

    rice = models.ForeignKey(
        Rice, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

