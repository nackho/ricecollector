from ssl import VERIFY_ALLOW_PROXY_CERTS
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('rice/', views.rice_index, name='index'),
    path('rice/<int:rice_id>/', views.rice_detail, name='detail'),
    path('rice/create/', views.RiceCreate.as_view(), name='rice_create'),
    path('rice/<int:pk>/update', views.RiceUpdate.as_view(), name='rice_update'),
    path('rice/<int:pk>/delete', views.RiceDelete.as_view(), name='rice_delete'),
]