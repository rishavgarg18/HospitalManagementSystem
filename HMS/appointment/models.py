from django.db import models
from patient.models import PatientBasicDetail
from doctor.models import DoctorBasicDetail

# Create your models here.
class appointments(models.Model):
    patient=models.ForeignKey(PatientBasicDetail,null=True,on_delete=models.SET_NULL)
    doctor=models.ForeignKey(DoctorBasicDetail,null=True,on_delete=models.SET_NULL)
    problem=models.CharField(max_length=500)
    existing_disease=models.CharField(max_length=500)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()
    status=models.CharField(max_length=200,default="TO MANAGER")
    add_date=models.DateTimeField(auto_now_add=True)


