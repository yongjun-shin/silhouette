from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.shortcuts import render
from . import views

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', index),
    path('login/', auth_views.LoginView.as_view(template_name = "login.html"), name = "login"),
    path('join/', include('user.urls')),  # user 앱의 urls.py를 include
    path('logout/', include('user.urls')),
    path('mypage/', views.mypage_view, name='mypage'),
    path('closet/', include('closet.urls')),
    path('weather/', views.weather_view, name='weather'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('trend/', views.trend_view, name='trend'),
    path("admin/", admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)