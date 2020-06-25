from django.db import models
from appointment.models import appointments

# Create your models here.
class PatientMedicalHistory(models.Model):
    appointment_id=models.ForeignKey(appointments,null=True,on_delete=models.SET_NULL)
    height=models.CharField(max_length=50)
    Weight=models.CharField(max_length=50)
    prescribed_medicine=models.CharField(max_length=500)
    blood_group=models.CharField(max_length=50)
    report_message=models.CharField(max_length=500)