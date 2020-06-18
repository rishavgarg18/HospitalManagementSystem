from django.urls import path
from .views import ManagerLogin


urlpatterns = [
    
   
    path('login/',ManagerLogin),
   

]