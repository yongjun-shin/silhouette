# user/views.py
from django.shortcuts import render, redirect
from .models import User

def login_view(request):
    return render(request, 'login.html')

def join_view(request):
    return render(request, 'join.html')

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
                user_pw=user_pw,
                user_name=user_name,
                user_email=user_email
            )
            user.save()
            return redirect('login')  # 회원가입 후 로그인 페이지로 리다이렉트

    return render(request, 'join.html')

def mypage_view(request):
    return render(request, 'mypage.html')