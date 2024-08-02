from django.contrib import admin
from .models import FoodItemInventory

# Register your models here.


@admin.register(FoodItemInventory)
class FoodItemInventoryAdmin(admin.ModelAdmin):
  list_display = ["name", "quantity"]