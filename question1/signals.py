import time
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(pre_save, sender=User)
def pre_handler(sender, instance, **kwargs):
    print(f"Pre Signal received for user: {instance.username}")
    time.sleep(5)  
    print("Pre Signal processing complete")


@receiver(post_save, sender=User)
def post_handler(sender, instance, **kwargs):
    print(f"Post Signal received for user: {instance.username}")
    time.sleep(5)  
    print("Signal processing complete")
