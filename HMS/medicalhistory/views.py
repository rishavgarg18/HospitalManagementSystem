from django.shortcuts import render
from .models import PatientMedicalHistory
import json
from django.http import JsonResponse
from appointment.models import appointments



def add_report(request):
    if request.method=="POST":
        data=json.loads(request.body)
        appointment_id=data['appointment_id_id']
        PatientMedicalHistory.objects.create(**data)
        appointments.objects.filter(id=appointment_id).update(status="CLOSED")
        return JsonResponse("OK",safe=False)

def view_report_patient(request):
    if request.method=="POST":
        data=json.loads(request.body)
        patient_id=data['patient_id']
        return_data=PatientMedicalHistory.objects.filter(appointment_id__patient_id=patient_id).values('id','appointment_id_id','height','Weight','prescribed_medicine','blood_group','report_message','appointment_id__doctor_id__first_name','appointment_id__doctor_id__last_name','appointment_id__doctor_id__email','appointment_id__doctor_id__phone_no','appointment_id__problem','appointment_id__existing_disease','appointment_id__appointment_date','appointment_id__appointment_time')
        return JsonResponse(list(return_data),safe=False)



        