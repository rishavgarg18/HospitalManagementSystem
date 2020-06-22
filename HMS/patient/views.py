from .models import PatientBasicDetail
from django.http import JsonResponse
import json

def PatientRegistration(request):
    if request.method=="POST":
        patient_data=json.loads(request.body)
        email=patient_data['email']
        if PatientBasicDetail.objects.filter(email=email).exists():
            return JsonResponse("EMAIL ALREADY REGISTERED",safe=False)
        else:
            PatientBasicDetail.objects.create(**patient_data)
            return JsonResponse("OK",safe=False)

def PatientLogin(request):
    if request.method=="POST":
        login_data=json.loads(request.body)
        email=login_data['email']
        password=login_data['password']
        if PatientBasicDetail.objects.filter(email__contains=email,password__contains=password).filter(email=email,password=password).exists():
            return_data=PatientBasicDetail.objects.filter(email=email).values()
            return JsonResponse(list(return_data),safe=False)
        else:
            return JsonResponse("Invalid Credentials",safe=False)

          
