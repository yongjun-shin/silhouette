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
    return render(request, 'acc.html')

def shoes_view(request):
    return render(request, 'shoes.html')

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

def get_outer(request):
    outers = Clothes.objects.filter(clothes_type='outer')
    return render(request, 'clothes.html', {'outers' : outers})
