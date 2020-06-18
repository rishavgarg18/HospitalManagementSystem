from django.urls import path
from .views import add_appointment,reception_view_appointment_pending


urlpatterns = [
    
    path('add/',add_appointment),
    path('receptionpending/',reception_view_appointment_pending),

    

]