from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from .models import Custom_user
import uuid

# Create your views here.

def create_user(request):
    try:
        myuuid = uuid.uuid4()
        with transaction.atomic():
            # This will trigger the post_save signal
            user = Custom_user.objects.create(username=f"testuser  id { str(myuuid)}")
            #An error to trigger a rollback
            raise Exception("Simulated transaction failure") # it will failed to create user instance.
            message = ""
    except Exception as e:
        message = 'faild to '
        print("Transaction failed:", e)
    
    return render(request, 'question3/user_created.html', {'user': user,  'message': message})
