from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ebook(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    cvr_url = models.CharField(max_length=2048)


    def __str__(self):
        return self.title


class CartItems(models.Model):
    title = models.CharField(max_length=50, null = True)
    price = models.FloatField(null=True)

class Product(models.Model):
    store = models.ForeignKey(Ebook, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Orders(models.Model):
    order_id = models.CharField(primary_key=True, max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    tableNumber = models.IntegerField()
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    orderStatus = models.CharField(max_length=100)
    paymentStatus = models.CharField(max_length=100)




class Crisp(models.Model):
    item = models.CharField(max_length=50)
    price = models.FloatField()

class WaffleUP(models.Model):
    item = models.CharField(max_length=50)
    price = models.FloatField()

def redir(store, id):
    products = Product.objects.filter(store=id)
    return products

