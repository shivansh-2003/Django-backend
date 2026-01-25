from rest_framework import serializers  
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta: 
        model = Product
        fields = ['id', 'model_id', 'title', 'content', 'price','sale_price'  ]

    def get_my_discount(self, obj):
        return obj.get_discount()