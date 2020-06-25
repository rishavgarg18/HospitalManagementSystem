from .models import ManagerBasicDetail
from django.http import JsonResponse
import json
from doctor.models import DoctorBasicDetail
from appointment.models import appointments
from patient.models import PatientBasicDetail

def ManagerLogin(request):
    if request.method=="POST":
        login_data=json.loads(request.body)
        username=login_data['username']
        password=login_data['password']
        if ManagerBasicDetail.objects.filter(username__contains=username,password__contains=password).filter(username=username,password=password).exists():
            return JsonResponse("OK",safe=False)
        else:
            return JsonResponse("Invalid Credentials",safe=False)



def not_approved_doctor_list(request):
    if request.method=="GET":
        return_data=DoctorBasicDetail.objects.filter(status="NOT APPROVED").values()
        return JsonResponse(list(return_data),safe=False)

def approved_doctor_list(request):
    if request.method=="GET":
        return_data=DoctorBasicDetail.objects.filter(status="APPROVED").values()
        return JsonResponse(list(return_data),safe=False)

def rejected_doctor_list(request):
    if request.method=="GET":
        return_data=DoctorBasicDetail.objects.filter(status="REJECTED").values()
        return JsonResponse(list(return_data),safe=False)


def approve_doctor(request):
    if request.method=="POST":
        data=json.loads(request.body)
        doctor_id=data['doctor_id']
        DoctorBasicDetail.objects.filter(id=doctor_id).update(status="APPROVED")
        return JsonResponse("OK",safe=False)

def reject_doctor(request):
    if request.method=="POST":
        data=json.loads(request.body)
        doctor_id=data['doctor_id']
        DoctorBasicDetail.objects.filter(id=doctor_id).update(status="REJECTED")
        return JsonResponse("OK",safe=False)
 

def all_patient_list(request):
    if request.method=="GET":
        patient_list=PatientBasicDetail.objects.all()
        return JsonResponse(list(patient_list),safe=False)

def patient_under_doctor(request):
    if request.method=="POST":
        data=json.loads(request.body)
        doctor_id=data['doctor_id']
        return_data=appointments.objects.filter(doctor_id=doctor_id).values('patient_id','patient__first_name','patient__last_name','patient__email','patient__phone_no','patient__address').distinct()
        return JsonResponse(list(return_data),safe=False)

