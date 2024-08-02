from django.db import models

# Create your models here.

class FoodItemInventory(models.Model):
  name = models.CharField(max_length=50)
  quantity = models.PositiveBigIntegerField()

  class Meta:
    verbose_name_plural = "FoodItemInventories"

  def __str__(self) -> str:
    return self.name