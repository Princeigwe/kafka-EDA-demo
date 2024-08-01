from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from . models import FoodItem
from django.http import Http404
from django.core.cache import cache

# Create your views here.

class CartItems(APIView):
  def post(self, request, food_id):
    try:
      food_item = FoodItem.objects.get(id=food_id)

      ## setting new cart for Prince only if there's none existing
      cart_owner = "prince_igwe_cart"
      my_cart = cache.add(key=cart_owner, value={"customer_name": "prince igwe", "items": [] }, timeout=1200)

      ## add food item to cart
      my_cart_items = cache.get(cart_owner)['items']
      cart_item = { "name": food_item.name, "price": int(food_item.price) }
      my_cart_items.append(cart_item)
      cache.set(key=cart_owner, value={ "customer_name": "prince igwe", "items": my_cart_items })

      updated_cart = cache.get(key=cart_owner)
      print(updated_cart)

      return Response({"message": "Added to cart"}, status=status.HTTP_200_OK)

    except FoodItem.DoesNotExist:
      raise Http404