from django.shortcuts import render

def store_view(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart_view(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout_view(request):
    context = {}
    return render(request, 'store/checkout.html', context)