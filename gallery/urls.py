from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('add_gallery/', views.add_gallery, name='add_gallery'),
    # path('del_gallery/<int:item_id>/', views.del_gallery, name='del_gallery'),
]