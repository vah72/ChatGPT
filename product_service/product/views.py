from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from .models import Product
from django.shortcuts import get_object_or_404

def product_list(request):
    products = Product.objects.all()

    response_data = []
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': str(product.price),
        }
        response_data.append(product_data)
    return JsonResponse(response_data, safe=False)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    resp = {}
    response_data = {
        'id': product.id,
        'name': product.name,
            'description': product.description,
            'price': str(product.price),
        }
    resp['data'] = response_data
    return JsonResponse(resp, safe=False)

