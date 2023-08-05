from django.urls import path
from . import views

urlpatterns = [
    path('', views.closet_view, name='closet'),
    path('clothes/', views.clothes_view, name='clothes'),
    path('add_clothes/', views.add_clothes, name='add_clothes'),
    path('del_clothes/<int:item_id>/', views.del_clothes, name='del_clothes'),
    path('acc/', views.acc_view, name='acc'),
    path('shoes/', views.shoes_view, name='shoes'),
]