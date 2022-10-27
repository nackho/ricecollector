from ssl import VERIFY_ALLOW_PROXY_CERTS
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('rice/', views.rice_index, name='index')
]