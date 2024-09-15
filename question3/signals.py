from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Custom_user
import time

@receiver(post_save, sender=Custom_user)
# Signal handled only after the transaction is committed.
def commit_handler(sender, instance, **kwargs):
    
    transaction.on_commit(lambda: print(f"Signal received for user: {instance.username}"))
    time.sleep(5)
    print("Signal processing complete")
