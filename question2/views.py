from django.shortcuts import render
from .models import custom_user
import uuid

def create_user(request):
    # This will trigger the post_save signal
    myuuid = uuid.uuid4()
    user = custom_user.objects.create(username=f"testuser  id { str(myuuid)}")
    print(str(user))
    return render(request, 'question2/user_created.html', {'user': user})
