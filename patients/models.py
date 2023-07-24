from django.db import models

# Create your models here.

class Doctors(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  username = models.CharField(max_length=50,default='username')
  password = models.CharField(max_length=50,default='password')

class Patients(models.Model):
    name = models.CharField(max_length=100)
    doctor = models.ManyToManyField(Doctors)