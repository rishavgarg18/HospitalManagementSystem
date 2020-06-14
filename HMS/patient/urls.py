from django.urls import path
from .views import PatientRegistration,PatientLogin


urlpatterns = [
    
    path('register/',PatientRegistration),
    path('login/',PatientLogin),

]