from django.forms import ModelForm
from .models import Picked

class PickedForm(ModelForm):
  class Meta:
    model = Picked
    fields = ['date', 'meal']
