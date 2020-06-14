from .models import PatientBasicDetail
from django.http import JsonResponse
import json

def PatientRegistration(request):
    if request.method=="POST":
        patient_data=json.loads(request.body)
        PatientBasicDetail.objects.create(**patient_data)
        return JsonResponse("OK",safe=False)

def PatientLogin(request):
    if request.method=="POST":
        login_data=json.loads(request.body)
        email=login_data['email']
        password=login_data['password']
        validate_login=PatientBasicDetail.objects.filter(email=email,password=password)
        if(validate_login):
            id=list(PatientBasicDetail.objects.filter(email=email).values())
            id_return=id[0]['id']

            return JsonResponse(id_return,safe=False)
        else:
            return JsonResponse("Invalid Credentials",safe=False)

          
