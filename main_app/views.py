from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def rice_index(request):
    return render(request, 'rice/index.html', { 'rice': rice })

class Rice:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, length, usage):
    self.name = name
    self.length = length
    self.usage = usage

rice = [
  Rice('Arborio Rice', 'medium', 'Risotto, rice pudding, soup'),
  Rice('Basmati Rice', 'long', 'pilaf, saffron rice'),
  Rice('Jasmine Rice', 'long', 'stir fry, Asian dishes')
]   