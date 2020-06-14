from django.shortcuts import render
from django.http import JsonResponse
from .models import appointments
import json

# Create your views here.
def add_appointment(request):
    if request.method=="POST":
        appointment_data=json.loads(request.body)
        appointments.objects.create(**appointment_data)
        return JsonResponse("OK",safe=False)
