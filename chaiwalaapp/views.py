from django.shortcuts import render
from django.db import models
from .models import *
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import modelformset_factory
from django.contrib.auth.models import User


# Create your views here.

from .forms import *

def ChaiwalaReg(request):

    form = ChaiwalaReg_Form()
    if request.method == 'POST':
        form = ChaiwalaReg_Form(request.POST)
        if form.is_valid():
            u = form.save()
            p = ChaiwalaReg_Model.objects.all()

            return render(request, 'display.html', {'p':p})
            #   return HttpResponseRedirect('/display')
        else:
            form_class = ChaiwalaReg_Form()

    return render(request, 'ChaiwalaReg.html', {
        'form': form,
    })

def CustomerReg(request):

    form = CustomerReg_Form()
    if request.method == 'POST':
        form = CustomerReg_Form(request.POST)
        if form.is_valid():
            u1 = form.save()
            p1 = CustomerReg_Model.objects.all()

            return render(request, 'display.html', {'p1':p1})
            #   return HttpResponseRedirect('/display')
        else:
            form_class = CustomerReg_Form()

    return render(request, 'CustomerReg.html', {
        'form': form,
    })

def display(request):
    p = ChaiwalaReg_Model.objects.all()

    return render(request, 'display.html', {'p':p})
            
    p1 = CustomerReg_Model.objects.all()

    return render(request, 'display.html', {'p1':p1})
  
def index(request):
    return render(request, 'index.html')
  



