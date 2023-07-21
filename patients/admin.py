from django.contrib import admin
from .models import Patients
from .models import Doctors

admin.site.register(Patients)
admin.site.register(Doctors)