from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

# View for showing all the product in the database

def all_products(request):
    

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

# Detailed product view

def detail_product(request, product_id):
    

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/detail_product.html', context)

    