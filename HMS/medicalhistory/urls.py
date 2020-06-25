from django.urls import path
from .views import add_report,view_report_patient

urlpatterns = [
    
    path('add/',add_report),
    path('viewpatient/',view_report_patient),
    

]