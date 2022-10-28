from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Rice, Dish
from .forms import PickedForm
from django.views.generic import ListView
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def rice_index(request):
    cats = Cat.objects.filter(user=request.user)
    return render(request, 'rice/index.html', { 'rice': rice })

def rice_index(request):
  rice = Rice.objects.all()
  return render(request, 'rice/index.html', { 'rice': rice })

@login_required
def rice_detail(request, rice_id):
    rice = Rice.objects.get(id=rice_id)
    id_list = rice.dishes.all().values_list('id')
    dishes_rice_doesnt_have = Dish.objects.exclude(id__in=id_list)
    picked_form = PickedForm()
    return render(request, 'rice/detail.html', { 'rice': rice, 'picked_form': picked_form, 'dishes': dishes_rice_doesnt_have})

@login_required
def add_picked(request, rice_id):
    form = PickedForm(request.POST)
    if form.is_valid():
        new_picked = form.save(commit=False)
        new_picked.rice_id = rice_id
        new_picked.save()
    return redirect ('detail', rice_id=rice_id)

class RiceCreate(CreateView):
    model = Rice
    fields = ['name', 'length', 'usage']
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
    success_url = '/rice/'

class RiceUpdate(LoginRequiredMixin, UpdateView):
    model = Rice
    fields = ['name', 'length', 'usage']

class RiceDelete(LoginRequiredMixin, DeleteView):
    model = Rice
    success_url = '/rice/'

@login_required
def assoc_dish(request, rice_id, dish_id):
  Rice.objects.get(id=rice_id).dishes.add(dish_id)
  return redirect('detail', rice_id=rice_id)

class DishList(LoginRequiredMixin, ListView):
  model = Dish

class DishDetail(LoginRequiredMixin, DetailView):
  model = Dish

class DishCreate(LoginRequiredMixin, CreateView):
  model = Dish
  fields = '__all__'

class DishUpdate(LoginRequiredMixin, UpdateView):
  model = Dish
  fields = ['name', 'ethnicity']

class DishDelete(LoginRequiredMixin, DeleteView):
  model = Dish
  success_url = '/dishes/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)