from django.db import models
import requests

# class Cart(models.Model):
#     user_id = models.CharField(max_length=50)
#     items = models.ManyToManyField('product_service.Product', through='CartItem')

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey('product_service.Product', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def get_user(self):
#         response = requests.get(f'http://localhost:8002/accounts/{self.cart.user_id}/')
#         user_data = response.json()
#         return user_data

#     def get_product(self):
#         response = requests.get(f'http://localhost:8001/api/products/{self.product_id}/')
#         product_data = response.json()
#         return product_data

class CartItem(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField(default=1)