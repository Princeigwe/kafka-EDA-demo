from django.contrib import admin
from .models import FoodItem, Order, OrderItem

# Register your models here.

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
  list_display = ["id", "name", "price"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ["id", "customer_name", "status", "created"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
  list_display = ["id", "name", "quantity", "unit_price", "price", "order"]