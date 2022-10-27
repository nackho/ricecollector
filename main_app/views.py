from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Rice
from django.views.generic import ListView
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

class RiceCreate(CreateView):
    model = Rice
    fields = '__all__'
    success_url = '/rice/'

class RiceUpdate(UpdateView):
    model = Rice
    fields = ['name', 'length', 'usage']

class RiceDelete(DeleteView):
    model = Rice
    success_url = '/rice/'