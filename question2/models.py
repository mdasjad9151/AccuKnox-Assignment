from django.db import models

# Create your models here.
class custom_user(models.Model):
    username =  models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.username
    