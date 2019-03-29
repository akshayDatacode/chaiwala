from django.urls import include, path
from django.conf.urls import url
from .views import * 

# urlpatterns = [
    
#     path('ChaiwalaReg', ChaiwalaReg, name='ChaiwalaReg'),
#     path('CustomerReg', CustomerReg, name='CustomerReg'),
#     path('display', display, name='display'),
#     path('index', index , name='index'),
    
           
# ]


from .views import *

urlpatterns = [
   path('landing', landing , name='landing'),
   
   path('dashboard', Chai_Order, name='dashboard'),
   
   url('^accounts/', include('django_registration.backends.activation.urls')),
   url('^accounts/', include('django.contrib.auth.urls')), 
]