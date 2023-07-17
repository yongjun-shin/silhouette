from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', index),
    path('login/', views.login_view, name='login'),
    path('join/', views.join_view, name='join'),
    path("admin/", admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)