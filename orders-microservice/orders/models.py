from django.db import models
import status

# Create your models here.

class Order(models.Model):
  customer_name = models.CharField(max_length=50)
  status        = models.CharField(max_length=20, choices=status.ORDER_STATUS, default="PLACED")
  created       = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return self.name


class OrderItem(models.Model):
  name       = models.CharField(max_length=50)
  quantity   = models.PositiveIntegerField(max_length=3)
  unit_price = models.DecimalField(max_digits=10, decimal_places=2)
  price      = models.DecimalField(max_digits=10, decimal_places=2)
  order      = models.ForeignKey(Order)

  def __str__(self) -> str:
    return self.name