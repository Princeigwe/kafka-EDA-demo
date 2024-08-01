from django.urls import path
from .views import CartItems, Order

urlpatterns = [
  path("cart/<int:food_id>", CartItems.as_view()),
  path("", Order.as_view())
]