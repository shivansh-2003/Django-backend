from django.db import models

# Create your models here.
class Product(models.Model):
    model_id = models.IntegerField(null=True,blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=15,decimal_places=2,default=99.99)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)


    def get_discount(self):
        return "122"