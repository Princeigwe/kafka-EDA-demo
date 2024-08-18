from threading import Thread
from utils.kafka.consumer import consume_kafka_messages

class ConsumeKafkaMessageThread(Thread):
  def __init__(self):
    Thread.__init__(self)
  
  def run(self):
    print("Kafka consumer thread running")
    consume_kafka_messages()