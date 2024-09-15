import threading
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Custom_user
import time

# Define an asynchronous signal handler using threading
@receiver(post_save, sender=Custom_user)
def async_signal_handler(sender, instance, **kwargs):
    def handle_signal():
        print(f"Signal received for user: {instance.username}")
        
        time.sleep(5)  # Delay
        print("Asynchronous signal processing complete")

    threading.Thread(target=handle_signal).start()
