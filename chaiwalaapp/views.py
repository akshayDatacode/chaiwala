from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import *
from .models import *
from django.forms import modelformset_factory
from .forms import *




def landing(request):
    return render(request,'registration/landing.html')
def dashboard(request):
    return render(request,'dashboard.html')

def Chai_Order(request):

    if request.method == 'POST':
        form = Chai_Order_From(request.POST)
        if form.is_valid():

            u = form.save()
            users = Chai_Order_Model.objects.all()

            return render(request, 'Chai_Order.html', {'users': users})
    else:
        
        form = Chai_Order_From()

    return render(request, 'dashboard.html', {'form': form})

