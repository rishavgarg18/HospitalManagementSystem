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
        
        if appointments.objects.filter(patient_id=patient_id,message="PENDING").exists():
            return JsonResponse("YOU CANNOT BOOK ANOTHER APPOINMENT UNTIL YOUR PREVIOUS APPOINTMENT IS NOT REJECTED",safe=False)
            
        else:
            appointments.objects.create(**appointment_data,message="PENDING")
            return JsonResponse("OK",safe=False)

def reception_view_appointment_pending(request):
    if request.method=="GET":
        return_data=appointments.objects.filter(status__contains="TO MANAGER").values('id','patient__email','patient__phone_no','appointment_date','appointment_time','problem','existing_disease','patient__first_name','patient__last_name')
        return JsonResponse(list(return_data),safe=False)

# def edit_appointment(request):
#     if request.method=="POST":
#         appointment_edit=json.loads(request.body)
#         appointment_id=appointment_edit['id']
#         appointment_date=appointment_edit['appointment_date']
#         appointment_time=appointment_edit['appointment_time']
#         appointments.objects.filter(id=appointment_id).update(appointment_date=appointment_date,appointment_time=appointment_time,status="TIME DATE CHANGED")
#         return JsonResponse("OK",safe=False)

def reject_appointment(request):
    if request.method=="POST":
        reject_data=json.loads(request.body)
        appointment_id=reject_data['appointment_id']
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
        appointment_date=str(data['appointment_date'])
        appointment_time=str(data['appointment_time'])
        appointment_time=appointment_time+":00"
       
        
        appointment_previous_data=appointments.objects.get(id=appointment_id)
      
        
        
        if str(appointment_previous_data.appointment_date)==appointment_date and str(appointment_previous_data.appointment_time)==appointment_time:
            appointments.objects.filter(id=appointment_id).update(doctor_id=doctor_id,status="PAYMENT PENDING")
        else:
            appointments.objects.filter(id=appointment_id).update(doctor_id=doctor_id,appointment_date=appointment_date,appointment_time=appointment_time,status="TIME DATE CHANGED")

        return JsonResponse("OK",safe=False)




def doctor_view_appointment_pending(request):
    if request.method=="POST":
        data=json.loads(request.body)
        doctor_id=data['doctor_id']
        return_data=appointments.objects.filter(doctor_id=doctor_id,status="TO DOCTOR").values('id','patient__email','patient__phone_no','appointment_date','appointment_time','problem','existing_disease','patient__first_name','patient__last_name')
        return JsonResponse(list(return_data),safe=False)

def patient_view(request):
    if request.method=="POST":
        data=json.loads(request.body)
        patient_id=data['patient_id']
        stats=appointments.objects.filter(patient_id=patient_id).latest('add_date')
        if stats.status=="REJECTED":
            return JsonResponse("YOUR APPOINTMENT HAS BEEN REJECTED",safe=False)
        elif stats.status=="PAYMENT PENDING":
            data=appointments.objects.filter(id=stats.id).values()
            return JsonResponse(list(data),safe=False)
        elif stats.status=="TIME DATE CHANGED":
            data=appointments.objects.filter(id=stats.id).values()
            return JsonResponse(list(data),safe=False)
        elif stats.status=="TO DOCTOR":
            return JsonResponse("YOUR APPOINTMENT IS TRANSFERED TO DOCTOR,WAITING FOR DOCTOR APPROVAL",safe=False)
        elif stats.status=="APPROVED":
            data=appointments.objects.filter(id=stats.id).values()
            return JsonResponse(list(data),safe=False)
        elif stats.status=="CLOSED":
            return JsonResponse("YOUR APPOINTMENT HAS BEEN CLOSED,DOCTOR HAS SUBMITTED YOUR REPORT,YOU CAN VIEW IT IN MEDICAL HISTORY SECTION",safe=False)

def patient_approve_appointment(request):
    if request.method=="POST":
        data=json.loads(request.body)
        appointment_id=data['appointment_id']
        appointments.objects.filter(id=appointment_id).update(status="TO DOCTOR",payment_info="TRUE")
        return JsonResponse("OK",safe=False)

def approve_appointment_doctor(request):
    if request.method=="POST":
        data=json.loads(request.body)
        appointment_id=data['appointment_id']
        appointments.objects.filter(id=appointment_id).update(status="APPROVED",message="APPROVED BY DOCTOR")
        return JsonResponse("OK",safe=False)