from django.shortcuts import render
from django.contrib.auth.models import User
import uuid

def create_user(request):
    myuuid = uuid.uuid4()
    # Befor Creating  new user Pre_save signal trigger after user created post_save signal trigger.
    user = User.objects.create(username=f"testuser  id { str(myuuid)}")
    return render(request, 'question1/user_created.html', {'user': user})
