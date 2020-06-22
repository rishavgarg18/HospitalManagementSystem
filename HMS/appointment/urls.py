from django.urls import path
from .views import add_appointment,reception_view_appointment_pending,edit_appointment
from .views import reject_appointment,send_doctor_list,forward_doctor


urlpatterns = [
    
    path('add/',add_appointment),
    path('receptionpending/',reception_view_appointment_pending),
    path('editappointment/',edit_appointment),
    path('rejectappointment/',reject_appointment),
    path('doctorlist/',send_doctor_list),
    path('forwardtodoctor/',forward_doctor),


    

]