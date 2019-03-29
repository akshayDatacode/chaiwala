# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Chai_Order_Model(models.Model):
    
    User = models.ForeignKey(User)
    Chaiwala = models.CharField(max_length=100)
    Quantity = models.CharField(max_length=255)
    
    

class Chai_Order_Model(models.Model):
    
    User = models.CharField(max_length=255 , default='NULL')
    Chaiwala = models.CharField(max_length=100)
    Quantity = models.CharField(max_length=255)
    
    

