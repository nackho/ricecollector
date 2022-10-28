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
    path('rice/<int:rice_id>/add_picked/', views.add_picked, name='add_picked'),
    path('rice/<int:rice_id>/assoc_dish/<int:dish_id>/', views.assoc_dish, name='assoc_dish'),
    path('dishes/', views.DishList.as_view(), name='dishes_index'),
    path('dishes/<int:pk>/', views.DishDetail.as_view(), name='dishes_detail'),
    path('dishes/create/', views.DishCreate.as_view(), name='dishes_create'),
    path('dishes/<int:pk>/update/', views.DishUpdate.as_view(), name='dishes_update'),
    path('dishes/<int:pk>/delete/', views.DishDelete.as_view(), name='dishes_delete'),

]