from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def join_view(request):
    return render(request, 'join.html')

def mypage_view(request):
    return render(request, 'mypage.html')