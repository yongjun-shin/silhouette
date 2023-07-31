from django.urls import path
from . import views

urlpatterns = [
    path('', views.join_view, name='join'),
    path('register/', views.register, name='register'),  # 회원가입을 처리하는 URL 패턴 추가
    path('login/', views.login, name='login'),  # 로그인 URL 패턴 추가
]