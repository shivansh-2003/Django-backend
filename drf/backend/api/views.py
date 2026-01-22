from products.models import Product
from django.forms.models import model_to_dict
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
from products.forms import ProductForm
from products.models import Product
@api_view(["GET","POST"]) 
def api_home(request, *args, **kwargs):
    if request.method == "GET":
        return Response({"message": "GET request"})
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "model_id", "title", "content", "price","sale_price" ])
    return Response(data)