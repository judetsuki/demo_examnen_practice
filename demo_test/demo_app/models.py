from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('manufacturer', on_delete=models.CASCADE)
    category =models.ForeignKey('Category')
    discount =
    stock =
    description =


class Order(models.Model):
    STATUS_CHOICES =[
        ('completed', 'завершен'),
        ('new', 'новый')
    ]
    order_date
    delivery_date = 
    status = delivery_address =
    receiver_name = 
    delivery_code = 
    user =

class OrderDetails(models.Model):
    order =
    product =
    order_quantity =


class Supplier(models.Model):
name

class Category(models.Model):
name

class Manufacturer(models.Model):
name

class DeliveryPoint(models.Model):
    address