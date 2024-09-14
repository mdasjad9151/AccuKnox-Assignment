import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import custom_user


@receiver(post_save, sender=custom_user)
def post_handler(sender, instance, **kwargs):
    print(f"Post Signal received for custom user: {instance.username}")
    time.sleep(5)  
    print("Signal processing complete")