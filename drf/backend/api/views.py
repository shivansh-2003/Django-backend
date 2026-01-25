from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    if request.method == "GET":
        queryset = Product.objects.all().order_by("-id")
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        return Response(ProductSerializer(instance).data, status=201)
    return Response(serializer.errors, status=400)