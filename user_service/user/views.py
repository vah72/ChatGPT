from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Account, Fullname, Address

def account_detail(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    fullname = account.fullname
    address = account.address
    res = {}
    response_data = {
        'id': account.id,
        'username': account.username,
        'fullname': {
            'first_name': fullname.first_name,
            'last_name': fullname.last_name,
        },
        'address': {
            'street': address.street,
            'city': address.city,
            'state': address.state,
            'zip_code': address.zip_code,
        },
    }
    res['data'] = response_data
    return JsonResponse(res)

def account_list(request):
    accounts = Account.objects.all()
    data = {'accounts' : list(accounts.values())}
    return JsonResponse(data)


