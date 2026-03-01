from django.shortcuts import render
from .models import Item

def home(request):
    items = Item.objects.all().order_by('-created_at')
    return render(request, 'core/home.html', {'items': items})
