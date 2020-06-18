from django.urls import path
from .views import DoctorRegistration,DoctorLogin


urlpatterns = [
    
    path('register/',DoctorRegistration),
    path('login/',DoctorLogin),
   

]