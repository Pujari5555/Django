from django.shortcuts import render
from .models import Category

def home(request):
    categories = Category.objects.all()
    return render(request, 'sarees_collections/home.html', {'categories': categories})
