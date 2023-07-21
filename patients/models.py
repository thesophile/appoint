from django.db import models

# Create your models here.

class Doctors(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Patients(models.Model):
    name = models.CharField(max_length=100)
    doctor = models.ManyToManyField(Doctors)