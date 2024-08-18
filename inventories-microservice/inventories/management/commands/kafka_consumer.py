from typing import Any
from django.core.management.base import BaseCommand
from threads import kafka_consumer_thread

class Command(BaseCommand):
  help = "Start Kafka consumer"

  def handle(self, *args: Any, **options: Any) -> str | None:
    kafka_consumer = kafka_consumer_thread.ConsumeKafkaMessageThread()
    kafka_consumer.start()