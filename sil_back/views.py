from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def mypage_view(request):
    return render(request, 'mypage.html')