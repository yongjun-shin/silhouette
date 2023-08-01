from django.urls import path
from . import views

urlpatterns = [
    path('', views.closet_view, name='closet'),
    path('clothes/', views.clothes_view, name='clothes'),
    path('acc/', views.acc_view, name='acc'),
    path('shoes/', views.shoes_view, name='shoes'),
]