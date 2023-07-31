from django.urls import path
from . import views

urlpatterns = [
    path('', views.closet_view, name='closet'),
]