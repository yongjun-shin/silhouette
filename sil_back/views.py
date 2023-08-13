from django.shortcuts import render, redirect
from closet.models import Clothes
from closet.models import Accessory
from closet.models import Shoes

def login_view(request):
    return render(request, 'login.html')

def mypage_view(request):
    outers = Clothes.objects.filter(clothes_type='outer').count()
    tops = Clothes.objects.filter(clothes_type='top').count()
    bottoms = Clothes.objects.filter(clothes_type='bottom').count()
    accs = Accessory.objects.all().count()
    shoeses = Shoes.objects.all().count()

    return render(request, 'mypage.html', {'outers':outers, 'tops':tops, 'bottoms':bottoms, 'accs':accs, 'shoeses':shoeses})