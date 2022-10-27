from django.shortcuts import render
from .models import Rice

from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def rice_index(request):
    return render(request, 'rice/index.html', { 'rice': rice })

def rice_index(request):
  rice = Rice.objects.all()
  return render(request, 'rice/index.html', { 'rice': rice })

def rice_detail(request, rice_id):
    rice = Rice.objects.get(id=rice_id)
    return render(request, 'rice/detail.html', { 'rice': rice})