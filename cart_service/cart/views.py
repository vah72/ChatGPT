# cart_service/cart/views.py
import requests
from django.http import JsonResponse
from .models import CartItem
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

USER_SERVICE_URL = 'http://localhost:8000'
PRODUCT_SERVICE_URL = 'http://localhost:8001'

def cart_list(request):
    user_id = request.GET.get('user_id')
    user_response = requests.get(f'{USER_SERVICE_URL}/accounts/{user_id}/')
    user_data = user_response.json()
    user = user_data['account']

    cart_items = CartItem.objects.filter(user=user)
    data = {'cart_items': []}
    for item in cart_items:
        product_response = requests.get(f'{PRODUCT_SERVICE_URL}/products/{item.product_id}/')
        product_data = product_response.json()
        product = product_data['product']

        product_data = {
            'id': product['id'],
            'name': product['name'],
            'description': product['description'],
            'price': product['price'],
            'quantity': item.quantity
        }
        data['cart_items'].append(product_data)

    return JsonResponse(data)


USER_SERVICE_URL = 'http://localhost:8000'

def get_user(request, cart_id):
    cartitem = get_object_or_404(CartItem, id=cart_id)
    user_id = cartitem.user_id
    response = requests.get(f'{USER_SERVICE_URL}/accounts/{user_id}/')
    data = response.json()
    user = data['data']
    return JsonResponse(user)


PRODUCT_SERVICE_URL = 'http://localhost:8001'

def get_product(request,cart_id):
    cartitem = get_object_or_404(CartItem, id=cart_id)
    product_id = cartitem.product_id
    response = requests.get(f'{PRODUCT_SERVICE_URL}/products/{product_id}/')
    data = response.json()
    product = data['data']
    return JsonResponse(product)

@csrf_exempt
def add_to_cart(request):
    user_id = request.POST.get('user_id')
    product_id = request.POST.get('product_id')
    quantity = request.POST.get('quantity', 1)

    user_response = requests.get(f'{USER_SERVICE_URL}/accounts/{user_id}/')
    user_data = user_response.json()
    user = user_data['data']

    product_response = requests.get(f'{PRODUCT_SERVICE_URL}/products/{product_id}/')
    product_data = product_response.json()
    product = product_data['data']

    cart_item, created = CartItem.objects.get_or_create(
        user_id=user_id,
        product_id=product_id,
        defaults={'quantity': quantity}
    )

    if not created:
        cart_item.quantity += int(quantity)
        cart_item.save()

    data = {
        'message': f'{product["name"]} added to cart',
        'cart_item': {
            'id': cart_item.id,
            'user': user_id,
            'product': product_id,
            'quantity': cart_item.quantity
        }
    }
    return JsonResponse(data)