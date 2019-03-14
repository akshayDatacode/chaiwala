from django.forms import ModelForm
from .models import *

class ChaiwalaReg_Form(ModelForm):
    class Meta:
        model = ChaiwalaReg_Model
        fields = '__all__'

class CustomerReg_Form(ModelForm):
    class Meta:
        model = CustomerReg_Model
        fields = '__all__'

