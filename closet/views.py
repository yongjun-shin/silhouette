from django.shortcuts import render

# Create your views here.
def closet_view(request):
    return render(request, 'closet.html')