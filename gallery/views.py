from django.shortcuts import render, redirect
from .models import Gallery

# Create your views here.
def gallery_view(request):
    return render(request, 'gallery.html')

# def clothes_view(request):
#     outers = Clothes.objects.filter(clothes_type='outer')
#     tops = Clothes.objects.filter(clothes_type='top')
#     bottoms = Clothes.objects.filter(clothes_type='bottom')
#     return render(request, 'clothes.html', {'outers' : outers, 'tops' : tops, 'bottoms': bottoms})

# def add_gallery(request):
#     if request.method == 'POST':
#         clothes_type = request.POST.get('clothes')  # radio 선택한 value
#         clothes_name = request.POST.get('name')  # Name이라는 label의 input에 적은 value
#         image_file = request.FILES.get('file')  # 선택한 image file

#         # DB에 저장
#         clothes = Clothes.objects.create(clothes_type=clothes_type,
#                                          clothes_name=clothes_name,
#                                          image_path=image_file)

#         # 저장 후 다른 페이지로 이동 또는 처리
#         return redirect('/closet/clothes/')  # 이동할 URL 또는 뷰 이름
#     return render(request, 'clothes.html')  # 뷰에서 처리할 HTML 파일의 경로

# def del_gallery(request, item_id):
#     if request.method == 'DELETE':
#         try:
#             clothes = Clothes.objects.get(pk=item_id)
#             clothes.delete()
#             return redirect('/closet/clothes/')
#         except Clothes.DoesNotExist:
#             print("You Can't Delete")

#     return render(request, 'clothes.html')
