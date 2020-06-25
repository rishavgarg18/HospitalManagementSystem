from django.urls import path
from .views import DoctorRegistration,DoctorLogin,all_approved_appointment


urlpatterns = [
    
    path('register/',DoctorRegistration),
    path('login/',DoctorLogin),
    path('allapprovedappointment/',all_approved_appointment),
   

]