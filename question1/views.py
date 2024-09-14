from django.shortcuts import render
from django.contrib.auth.models import User
import uuid

def create_user(request):
    # Create a new user to trigger the post_save signal
    myuuid = uuid.uuid4()
    user = User.objects.create(username=f"testuser  id { str(myuuid)}")
    return render(request, 'question1/user_created.html', {'user': user})
