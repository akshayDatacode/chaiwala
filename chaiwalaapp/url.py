from django.urls import include, path
from .views import * 

urlpatterns = [
    
    path('ChaiwalaReg', ChaiwalaReg, name='ChaiwalaReg'),
    path('CustomerReg', CustomerReg, name='CustomerReg'),
    path('display', display, name='display'),
    path('index', index , name='index'),
    
           
]