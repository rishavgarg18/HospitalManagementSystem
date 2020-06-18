from .models import ManagerBasicDetail
from django.http import JsonResponse
import json

def ManagerLogin(request):
    if request.method=="POST":
        login_data=json.loads(request.body)
        username=login_data['username']
        password=login_data['password']
        if ManagerBasicDetail.objects.filter(username=username,password=password).exists():
            return JsonResponse("OK",safe=False)
        else:
            return JsonResponse("Invalid Credentials",safe=False)



