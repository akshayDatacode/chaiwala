
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ChaiwalaReg_Model(models.Model):

    userid = models.CharField(max_length=100)
    name= models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class CustomerReg_Model(models.Model):

    userid = models.CharField(max_length=100)
    name= models.CharField(max_length=255)
    password = models.CharField(max_length=255)
