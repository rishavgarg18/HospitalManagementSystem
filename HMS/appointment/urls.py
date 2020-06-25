from django.urls import path
from .views import add_appointment,reception_view_appointment_pending
from .views import reject_appointment,send_doctor_list,forward_doctor,doctor_view_appointment_pending
from .views import patient_view,patient_approve_appointment,approve_appointment_doctor

urlpatterns = [
    
    path('add/',add_appointment),
    path('receptionpending/',reception_view_appointment_pending),
    path('doctorpending/',doctor_view_appointment_pending),
    path('rejectappointment/',reject_appointment),
    path('doctorlist/',send_doctor_list),
    path('forwardtodoctor/',forward_doctor),
    path('patientview/',patient_view),
    path('patientapproveappointment/',patient_approve_appointment),
    path('doctorapproveappointment/',approve_appointment_doctor),
    


    

]