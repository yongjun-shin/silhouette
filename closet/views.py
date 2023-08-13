from django.shortcuts import render, redirect
from .models import Clothes
from .models import Accessory
from .models import Shoes

# Create your views here.
def closet_view(request):
    return render(request, 'closet.html')

def clothes_view(request):
    outers = Clothes.objects.filter(clothes_type='outer')
    tops = Clothes.objects.filter(clothes_type='top')
    bottoms = Clothes.objects.filter(clothes_type='bottom')
    return render(request, 'clothes.html', {'outers' : outers, 'tops' : tops, 'bottoms': bottoms})

def acc_view(request):
    accs = Accessory.objects.all()
    return render(request, 'acc.html', {'accs' : accs})

def shoes_view(request):
    shoeses = Shoes.objects.all()
    return render(request, 'shoes.html', {'shoeses': shoeses})

def add_clothes(request):
    if request.method == 'POST':
        clothes_type = request.POST.get('clothes')  # radio 선택한 value
        clothes_name = request.POST.get('name')  # Name이라는 label의 input에 적은 value
        image_file = request.FILES.get('file')  # 선택한 image file

        # DB에 저장
        clothes = Clothes.objects.create(clothes_type=clothes_type,
                                         clothes_name=clothes_name,
                                         image_path=image_file)

        # 저장 후 다른 페이지로 이동 또는 처리
        return redirect('/closet/clothes/')  # 이동할 URL 또는 뷰 이름
    return render(request, 'clothes.html')  # 뷰에서 처리할 HTML 파일의 경로

def add_acc(request):
    if request.method == 'POST':
        acc_name = request.POST.get('name') 
        image_file = request.FILES.get('file')

        acc = Accessory.objects.create(acc_name=acc_name,
                                         image_path=image_file)

        return redirect('/closet/acc/') 
    return render(request, 'clothes.html')

def add_shoes(request):
    if request.method == 'POST':
        shoes_name = request.POST.get('name') 
        image_file = request.FILES.get('file')

        shoes = Shoes.objects.create(shoes_name=shoes_name,
                                         image_path=image_file)

        return redirect('/closet/shoes/') 
    return render(request, 'clothes.html')

def del_clothes(request, item_id):
    if request.method == 'DELETE':
        try:
            clothes = Clothes.objects.get(pk=item_id)
            clothes.delete()
            return redirect('/closet/clothes/')
        except Clothes.DoesNotExist:
            print("You Can't Delete")

    return render(request, 'clothes.html')

def del_acc(request, item_id):
    if request.method == 'DELETE':
        try:
            acc = Accessory.objects.get(pk=item_id)
            acc.delete()
            return redirect('/closet/acc/')
        except Accessory.DoesNotExist:
            print("You Can't Delete")

    return render(request, 'clothes.html')

def del_shoes(request, item_id):
    if request.method == 'DELETE':
        try:
            shoes = Shoes.objects.get(pk=item_id)
            shoes.delete()
            return redirect('/closet/shoes/')
        except Shoes.DoesNotExist:
            print("You Can't Delete")

    return render(request, 'clothes.html')

def get_outer(request):
    outers = Clothes.objects.filter(clothes_type='outer')
    return render(request, 'clothes.html', {'outers' : outers})
def get_top(request):
    tops = Clothes.objects.filter(clothes_type='top')
    return render(request, 'clothes.html', {'tops' : tops})
def get_bottom(request):
    bottoms = Clothes.objects.filter(clothes_type='bottom')
    return render(request, 'clothes.html', {'bottoms' : bottoms})
