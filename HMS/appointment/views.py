from django.shortcuts import render
from django.http import JsonResponse
from .models import appointments
import json

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
        return_data=appointments.objects.filter(status="TO MANAGER").values()
        return JsonResponse(list(return_data),safe=False)
