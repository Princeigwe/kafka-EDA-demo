from inventories.models import FoodItemInventory

def update_inventory(messages):
  for message in messages:
    for item in message.value['items']:
      food_item = FoodItemInventory.objects.get(name=item['name'])
      current_food_item_quantity = food_item.quantity
      new_food_item_quantity = current_food_item_quantity - item['quantity']
      food_item.quantity = new_food_item_quantity
      food_item.save()

      print(f" Quantity of {food_item.name} has now reduced from {current_food_item_quantity} to {food_item.quantity}. ")