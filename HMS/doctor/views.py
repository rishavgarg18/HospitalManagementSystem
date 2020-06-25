from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import DoctorBasicDetail
from appointment.models import appointments
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


def all_approved_appointment(request):
    if request.method=="POST":
        data=json.loads(request.body)
        doctor_id=data['doctor_id']
        return_data=appointments.objects.filter(doctor_id=doctor_id,status="APPROVED").values('id','patient__email','patient__phone_no','appointment_date','appointment_time','problem','existing_disease','patient__first_name','patient__last_name')
        return JsonResponse(list(return_data),safe=False)