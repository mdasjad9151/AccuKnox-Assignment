from django.shortcuts import render
from .models import Custom_user
import uuid

def create_user(request):
    myuuid = uuid.uuid4()
    user = Custom_user.objects.create(username=f"testuser  id { str(myuuid)}")
    return render(request, 'question1Async/user_created.html', {'user': user})
