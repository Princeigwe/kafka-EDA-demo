from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import FoodItem, Order as OrderModel, OrderItem
from . serializers import CartSerializer
from django.http import Http404
from django.core.cache import cache

# Create your views here.

cart_owner = "prince_igwe_cart"

class CartItems(APIView):
  def post(self, request, food_id):
    try:
      serializer = CartSerializer(data=request.data)
      if serializer.is_valid():
        item_quantity = request.data['quantity']
        food_item = FoodItem.objects.get(id=food_id)

        ## setting new cart for Prince only if there's none existing
        cache.add(key=cart_owner, value={"customer_name": "prince igwe", "items": [] }, timeout=1200)

        ## add food item to cart
        my_cart_items = cache.get(cart_owner)['items']
        cart_item = { "name": food_item.name, "price": int(food_item.price), "quantity": item_quantity }
        my_cart_items.append(cart_item)
        cache.set(key=cart_owner, value={ "customer_name": "prince igwe", "items": my_cart_items })

        updated_cart = cache.get(key=cart_owner)
        print(updated_cart)

        return Response({"message": "Added to cart"}, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except FoodItem.DoesNotExist:
      raise Http404


class Order(APIView):
  # place an order
  def post(self, request):
    my_cart = cache.get(key=cart_owner)
    order = OrderModel.objects.create(customer_name=my_cart['customer_name'])
    order.save()

    my_cart_items = cache.get(cart_owner)['items']
    for item in my_cart_items:
      item_name = item['name']
      item_quantity = item['quantity']
      item_unit_price = item['price']
      price = item_unit_price * item_quantity

      order_item = OrderItem.objects.create(name=item_name, quantity=item_quantity, unit_price=item_unit_price, price=price, order=order)
      order_item.save()
    
    return Response({"message": "Order has been placed for delivery."}, status=status.HTTP_200_OK)