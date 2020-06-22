from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import DoctorBasicDetail
# Create your views here.


def DoctorRegistration(request):
    if request.method=="POST":
        doctor_data=json.loads(request.body)
        email=doctor_data['email']
        if DoctorBasicDetail.objects.filter(email=email).exists():
            return JsonResponse("EMAIL ALREADY REGISTERED",safe=False)
        else:
            DoctorBasicDetail.objects.create(**doctor_data)
            return JsonResponse("OK",safe=False)

def DoctorLogin(request):
    if request.method=="POST":
        login_data=json.loads(request.body)
        email=login_data['email']
        password=login_data['password']
        if DoctorBasicDetail.objects.filter(email__contains=email,password__contains=password).filter(email=email,password=password).exists():
            return_data=DoctorBasicDetail.objects.filter(email=email).values()
            return JsonResponse(list(return_data),safe=False)
        else:
            return JsonResponse("Invalid Credentials",safe=False)
