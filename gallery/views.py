from django.shortcuts import render, redirect
from .models import Gallery
from closet.models import Clothes, Accessory, Shoes

# Create your views here.
def gallery_view(request):
    outers = Clothes.objects.filter(clothes_type='outer')
    tops = Clothes.objects.filter(clothes_type='top')
    bottoms = Clothes.objects.filter(clothes_type='bottom')
    accs = Accessory.objects.all()
    shoeses = Shoes.objects.all()
    gallerys = Gallery.objects.all()
    return render(request, 'gallery.html', {'outers' : outers, 'tops' : tops, 'bottoms': bottoms, 'accs': accs, 'shoeses':shoeses, 'gallerys': gallerys})

def add_gallery(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        outer = request.POST.get('outer') 
        top = request.POST.get('top')
        pants = request.POST.get('pants') 
        acc = request.POST.get('acc')
        shoes = request.POST.get('shoes')
        memo = request.POST.get('memo')
 
        Gallery.objects.create(title=title,
                                outer=outer,
                                top=top,
                                pants=pants,
                                acc=acc,
                                shoes=shoes,
                                memo=memo)
  
        return redirect('/gallery/')
    return render(request, 'gallery.html') 

def del_gallery(request, item_id):
    if request.method == 'DELETE':
        try:
            gallery = Gallery.objects.get(pk=item_id)
            gallery.delete()
            return redirect('/gallery/')
        except Gallery.DoesNotExist:
            print("You Can't Delete")

    return render(request, 'gallery.html')
