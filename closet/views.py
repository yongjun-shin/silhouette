from django.shortcuts import render

# Create your views here.
def closet_view(request):
    return render(request, 'closet.html')

def clothes_view(request):
    return render(request, 'clothes.html')

def acc_view(request):
    return render(request, 'acc.html')

def shoes_view(request):
    return render(request, 'shoes.html')