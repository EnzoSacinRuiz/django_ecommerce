from django.shortcuts import render
from .models import Product  # Make sure to import the Product model

def store(request):
    products = Product.objects.all()  # Fetch all products from the database
    context = {'products': products}  # Add the products to the context
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
