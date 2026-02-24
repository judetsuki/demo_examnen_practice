from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('manufacturer', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    discount = models.IntegerField(default=0)
    stock = models.PositiveBigIntegerField(default=0)
    description = models.TextField()


class Order(models.Model):
    STATUS_CHOICES = [
        ('completed', 'завершен'),
        ('new', 'новый')
    ]
    order_date = models.DateField()
    delivery_date = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES)
    delivery_address = models.TextField()
    receiver_name = models.TextField()
    delivery_code = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)


class OrderDetails(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    order_quantity = models.PositiveIntegerField(default=1)


class Supplier(models.Model):
    name = models.TextField()


class Category(models.Model):
    name = models.TextField()


class Manufacturer(models.Model):
    name = models.TextField()


class DeliveryPoint(models.Model):
    address = models.TextField()


class UserToGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)


class Group(models.Model):
    role = models.CharField(max_length=255)
