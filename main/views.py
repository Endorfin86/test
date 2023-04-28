from django.shortcuts import render
from .models import Items

def home(request):
    items = Items.objects.all()
    return render(request, 'main/home.html', {'items': items})

def page(request, **kwargs):
    return render(request, 'main/page.html', {'select': kwargs})
