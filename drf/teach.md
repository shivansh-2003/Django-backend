# DRF Tutorial Notes (Current State)

This project is a small Django + Django REST Framework (DRF) learning setup.
It has a Django project (`cfehome`) with two apps:
- `api` for request/response handling.
- `products` for the data model and serialization.

Below is what is implemented so far, how the request flow works, and how the pieces
connect.

## What Is Implemented

### Project + Apps
- **Project:** `backend/cfehome`
- **Apps:** `api`, `products` (both are installed in `settings.py`).

```17:41:drf/backend/cfehome/settings.py
INSTALLED_APPS = [
    # ...
    'api',
    'products',
]
```

### Product Model
`products.models.Product` is the main database model.

```4:16:drf/backend/products/models.py
class Product(models.Model):
    model_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "122"
```

Key ideas:
- **Fields define DB columns.**
- `sale_price` is a computed property (not stored in DB).
- `get_discount` is a method used by the serializer.

### Serializer
`products.serializers.ProductSerializer` converts a `Product` instance to JSON.

```1:11:drf/backend/products/serializers.py
class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'model_id', 'title', 'content', 'price', 'sale_price']

    def get_my_discount(self, obj):
        return obj.get_discount()
```

Key ideas:
- **Serializer turns model objects into JSON-ready data.**
- `sale_price` comes from the model property.
- `my_discount` is computed by `get_my_discount`.

### API View
`api.views.api_home` is the single API endpoint currently wired.

```1:17:drf/backend/api/views.py
@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
    if request.method == "GET":
        return Response({"message": "GET request"})
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)
```

Key ideas:
- **DRF view + `Response`** returns JSON automatically.
- GET returns a simple message for now.
- POST randomly selects one product and serializes it.

### URL Routing
Project routes include the API app, and the API app points the root `/api/` path
to `api_home`.

```20:23:drf/backend/cfehome/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

```4:6:drf/backend/api/urls.py
urlpatterns = [
    path('', views.api_home),
]
```

Result: `http://127.0.0.1:8000/api/` hits `api_home`.

### Migrations
You have migrations for `Product`:
- `0001_initial.py` (base model)
- `0002_product_model_id.py` (adds `model_id`)

These must be applied with `python3 manage.py migrate`.

## How the Flow Works (Theory)

1. **Client sends a request** (browser or `pyclient/basic.py`) to `/api/`.
2. **URL router** in `cfehome/urls.py` sends it to `api/urls.py`.
3. **View function** `api_home` runs.
4. **View logic:**
   - GET: returns a simple JSON message.
   - POST: fetches a `Product`, serializes it, returns JSON.
5. **Serializer** converts the Django model instance into JSON-friendly data.
6. **Response** returns the JSON to the client.

## Why You Saw "GET request"

Your client was doing a GET, and the view exits early for GET:
```10:13:drf/backend/api/views.py
if request.method == "GET":
    return Response({"message": "GET request"})
```
So it never reached the product query on GET.

## Suggested Next Steps (Learning Progression)
- Add `POST` body handling to create a new `Product`.
- Use `ProductSerializer(data=request.data)` to validate input.
- Return a list of products on GET instead of a message.
- Add proper error handling for empty tables.

## Mermaid Diagram (Request Flow)

```mermaid
flowchart TD
    A[Client: browser or pyclient] --> B[/api/]
    B --> C[cfehome/urls.py include api.urls]
    C --> D[api/urls.py path '' -> api_home]
    D --> E{Request method?}
    E -->|GET| F[Return {"message": "GET request"}]
    E -->|POST| G[Query Product model]
    G --> H[ProductSerializer]
    H --> I[DRF Response JSON]
```
