from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'shop/product.html', {'products': products})

def index2(request):
    categories = Category.objects.all()
    return render(request, 'shop/category.html', {'categories': categories})

# Main page
def main_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop/main.html', {'products': products, 'categories': categories})

# Product
def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 1)  # Show 1 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/product.html', {'page_obj': page_obj})

# Category
def category_list(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 1)  # Show 1 categories per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/category.html', {'page_obj': page_obj})

# Create product
def create_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        product_qty = request.POST.get('product_qty')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        product = Product(title=title, price=price, product_qty=product_qty, category=category)
        product.save()
        return redirect('main_page')
    
    categories = Category.objects.all()
    return render(request, 'shop/create_product.html', {'categories': categories, 'products': Product.objects.all()})


# Create category
def create_category(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = Category(title=title)
        category.save()
        return redirect('main_page')
    return render(request, 'shop/create_category.html', {'categories': Category.objects.all()})

# Read product
def read_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/read_product.html', {'product': product})

# Read category
def read_category(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, 'shop/read_category.html', {'category': category})

# Update product
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        product_qty = request.POST.get('product_qty')
        category_id = request.POST.get('category')
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return render(request, 'shop/update_product.html', {
                'product': product,
                'categories': Category.objects.all(),
                'error_message': 'Категорія не знайдена'
            })
            
        product.title = title
        product.price = price
        product.product_qty = product_qty
        product.category = category

        product.save()
        return redirect('main_page')
    
    categories = Category.objects.all()
    return render(request, 'shop/update_product.html', {'product': product, 'categories': categories})

# Update category
def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        category.title = request.POST.get('title')
        category.save()
        return redirect('main_page')
    
    return render(request, 'shop/update_category.html', {'category': category})

# Delete product
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('main_page')
    
    return render(request, 'shop/delete_product.html', {'product': product})

# Delete category
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('main_page')
    
    return render(request, 'shop/delete_category.html', {'category': category})