from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'shop/product.html', {'products': products})

def index2(request):
    categories = Category.objects.all()
    return render(request, 'shop/category.html', {'categories': categories})