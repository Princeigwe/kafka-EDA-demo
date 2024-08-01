from django.db import models
from . import status

# Create your models here.

class FoodItem(models.Model):
  name       = models.CharField(max_length=50)
  price      = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self) -> str:
    return self.name

class Order(models.Model):
  customer_name = models.CharField(max_length=50)
  status        = models.CharField(max_length=20, choices=status.ORDER_STATUS, default="PLACED")
  created       = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return self.name


class OrderItem(models.Model):
  name       = models.CharField(max_length=50)
  quantity   = models.PositiveIntegerField()
  unit_price = models.DecimalField(max_digits=10, decimal_places=2)
  price      = models.DecimalField(max_digits=10, decimal_places=2)
  order      = models.ForeignKey(Order, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return self.name