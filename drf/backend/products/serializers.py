from rest_framework import serializers  
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'model_id', 'title', 'content', 'price','sale_price']