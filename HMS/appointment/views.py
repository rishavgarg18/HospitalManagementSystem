from django.shortcuts import render
from django.http import JsonResponse
from .models import appointments
import json
from patient.models import PatientBasicDetail
from doctor.models import DoctorBasicDetail

# Create your views here.
def add_appointment(request):
    if request.method=="POST":
        appointment_data=json.loads(request.body)
        patient_id=appointment_data['patient_id']
        
        if appointments.objects.filter(patient_id=patient_id,status="TO MANAGER").exists():
            return JsonResponse("YOU CANNOT BOOK ANOTHER APPOINMENT UNTIL YOUR PREVIOUS APPOINTMENT IS NOT REJECTED",safe=False)
            
        else:
            appointments.objects.create(**appointment_data)
            return JsonResponse("OK",safe=False)

def reception_view_appointment_pending(request):
    if request.method=="GET":
        return_data=appointments.objects.filter(status__contains="TO MANAGER").values('id','patient__email','patient__phone_no','appointment_date','appointment_time','problem','existing_disease','patient__first_name','patient__last_name')
        return JsonResponse(list(return_data),safe=False)

def edit_appointment(request):
    if request.method=="POST":
        appointment_edit=json.loads(request.body)
        appointment_id=appointment_edit['id']
        appointment_date=appointment_edit['appointment_date']
        appointment_time=appointment_edit['appointment_time']
        appointments.objects.filter(id=appointment_id).update(appointment_date=appointment_date,appointment_time=appointment_time,status="TO PATIENT",message="PATIENT APPROVAL")
        return JsonResponse("OK",safe=False)

def reject_appointment(request):
    if request.method=="POST":
        reject_data=json.loads(request.body)
        appointment_id=reject_data['id']
        message=reject_data['message']
        appointments.objects.filter(id=appointment_id).update(status="REJECTED",message=message)
        return JsonResponse("OK",safe=False)

def send_doctor_list(request):
    if request.method=="POST":
        department=json.loads(request.body)
        department_name=department['department']

        doctor_list=DoctorBasicDetail.objects.filter(department=department_name).values('first_name','last_name','id')
        return JsonResponse(list(doctor_list),safe=False)

def forward_doctor(request):
    if request.method=="POST":
        data=json.loads(request.body)
        doctor_id=data['doctor_id']
        appointment_id=data['appointment_id']
        appointments.objects.filter(id=appointment_id).update(doctor_id=doctor_id,status="TO DOCTOR")
        return JsonResponse("OK",safe=False)