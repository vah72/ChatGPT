from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    product_description = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField()

    def get_product_name(self, obj):
        return obj.get_product()['name']

    def get_product_description(self, obj):
        return obj.get_product()['description']

    def get_product_price(self, obj):
        return obj.get_product().get_price()

    class Meta:
        model = CartItem
        fields = ('id', 'product_id', 'quantity', 'product_name', 'product_description', 'product_price')
