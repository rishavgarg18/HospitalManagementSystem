from django.urls import path
from .views import add_appointment


urlpatterns = [
    
    path('add/',add_appointment),
    

]