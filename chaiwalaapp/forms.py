from django.forms import ModelForm
from chaiwalaapp.models import Chai_Order_Model

class Chai_Order_From(ModelForm):
    class Meta:
        model = Chai_Order_Model
        fields = ['User','Chaiwala', 'Quantity']
