from django.urls import path
from .views import ManagerLogin,not_approved_doctor_list,approve_doctor,reject_doctor,approved_doctor_list
from .views import rejected_doctor_list

urlpatterns = [
    
   
    path('login/',ManagerLogin),
    path('notapproveddoctorlist/',not_approved_doctor_list),
    path('approveddoctorlist/',approved_doctor_list),
    path('rejecteddoctorlist/',rejected_doctor_list),
    path('approvedoctor/',approve_doctor),
    path('rejectdoctor/',reject_doctor),
   
   

]