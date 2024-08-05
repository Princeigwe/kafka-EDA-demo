from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

producer = KafkaProducer(bootstrap_servers="localhost:29092",
                        value_serializer=lambda m: json.dumps(m).encode('ascii'),
                        api_version=(2, 0, 0)
)

topic = "orders"

def update_inventory(ordered_items):
  future = producer.send(topic, ordered_items)
  try:
    metadata = future.get()
    print(metadata)
    # print(" ")
    # print(f" {ordered_items}'s ordered items sent")
  except KafkaError as e:
    print(e)
