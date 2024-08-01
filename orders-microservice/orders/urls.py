from django.urls import path
from .views import CartItems

urlpatterns = [
  path("cart/<int:food_id>", CartItems.as_view())
]