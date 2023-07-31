# user/views.py
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password

def login_view(request):
    return render(request, 'login.html')

def join_view(request):
    return render(request, 'join.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pw')

        try:
            user = User.objects.get(user_email=email)
            if user.user_pw == password:
                # 로그인 성공 시 사용자를 로그인 상태로 처리
                request.session['user'] = user.id
                print('login success')
                return redirect('/')  # 로그인 성공 후 마이페이지 또는 다른 페이지로 리다이렉트
            else:
                # 비밀번호 불일치
                messages.error(request, '유효하지 않은 로그인 정보입니다.')
                return redirect('login')
        except User.DoesNotExist:
            # 사용자가 존재하지 않음
            messages.error(request, '유효하지 않은 로그인 정보입니다.')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_view(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('login')

def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('name', '')
        user_email = request.POST.get('email', '')
        user_pw = request.POST.get('pw', '')
        user_pw_confirm = request.POST.get('pw-confirm', '')
        
        if (user_pw or user_pw_confirm or user_name or user_email) == '':
            print("All fields must be filled.")
            return redirect('join')
        elif user_pw != user_pw_confirm:
            print("Passwords do not match.")
            return redirect('join')
        else:
            user = User(
                user_pw=make_password(user_pw),
                user_name=user_name,
                user_email=user_email
            )
            user.save()
            return redirect('login')  # 회원가입 후 로그인 페이지로 리다이렉트

    return render(request, 'join.html')

def mypage_view(request):
    return render(request, 'mypage.html')