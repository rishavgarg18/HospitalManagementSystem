from django.db import models

# Create your models here.

class DoctorBasicDetail(models.Model):
    department=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    age=models.CharField(max_length=10)
    gender=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    password=models.CharField(max_length=100)
    degree=models.CharField(max_length=100,null=True)
    previous_exp=models.IntegerField(null= True)
    status=models.CharField(max_length=50,default="NOT APPROVED")
    