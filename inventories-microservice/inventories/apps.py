from django.apps import AppConfig
import os
from django.core.management import call_command


class InventoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventories'

    def ready(self) -> None:
        if os.environ.get('RUN_MAIN'):
            print("hello kafka...")
            call_command('kafka_consumer')
