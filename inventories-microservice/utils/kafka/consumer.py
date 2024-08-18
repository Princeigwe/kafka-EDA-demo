from kafka import KafkaConsumer
import json
from utils.update_inventory import update_inventory

def consume_kafka_messages():
  topics = ['orders']

  consumer = KafkaConsumer(bootstrap_servers="localhost:29092",
                          value_deserializer=lambda m: json.loads(m.decode('ascii')),
                          group_id="inventory_relation",
                          auto_commit_interval_ms=1000,
                          api_version=(2, 0, 0)
  )

  consumer.subscribe(topics)

  while True:
    all_records = consumer.poll(timeout_ms=100, max_records=100)

    for topic_partition, messages in all_records.items():
      if topic_partition.topic == "orders":
        update_inventory(messages)
