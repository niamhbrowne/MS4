from django.shortcuts import render
from .models import Item

# Create your views here.


def get_home(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/home.html', context)
