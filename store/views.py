from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime

def store_view(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_order_items
    else:
        items = []
        order = {'get_order_total': 0, 'get_order_items': 0, 'check_shipping': False}
        cart_items = order['get_order_items']

    products = Product.objects.all()
    
    context = {
        'items': items,
        'order': order,
        'products': products,
        'cart_items': cart_items,
    }
    return render(request, 'store/store.html', context)

def cart_view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_order_items
    else:
        items = []
        order = {'get_order_total': 0, 'get_order_items': 0, 'check_shipping': False}
        cart_items = order['get_order_items']

    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
    }
    return render(request, 'store/cart.html', context)

def checkout_view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_order_items
    else:
        items = []
        order = {'get_order_total': 0, 'get_order_items': 0, 'check_shipping': False}
        cart_items = order['get_order_items']

    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
    }
    return render(request, 'store/checkout.html', context)

def update_item_view(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    print('ProductId', product_id)
    print('Action', action)

    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, customer = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = (order_item.quantity) + 1
    elif action == 'remove':
        order_item.quantity = (order_item.quantity) - 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()
    return JsonResponse("Item was added", safe=False)

def process_order(request):
    trx_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)
        
    total = float(data['form']['total'])
    order.trx_id = trx_id

    if total == order.get_order_total:
        order.complete = True
    order.save()

    if order.check_shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
            )
        print(ShippingAddress.objects)
    return JsonResponse('payment submitted', safe=False)