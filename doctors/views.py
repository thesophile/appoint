from django.shortcuts import render
from patients.models import Doctors
from patients.models import Patients

# Create your views here.





def doctors(request):
    doctor_objects = Doctors.objects.all()

    doctor_patients= []

    for doctor_object in doctor_objects:
        
        #get the queryset of all patients under a doctor
        patients_qs = doctor_object.patients_set.all()
        patient_list = list(patients_qs)
        doctor_patients.append(patient_list)


    
    doctor = Doctors.objects.all().values()
    
    master_list = zip(doctor_objects, doctor_patients) 

    context = {
        'doctor_objects': doctor_objects,
        'doctor_patients': doctor_patients,
        'master_list':master_list,
    }
        
    return render(request,'doctors.html',context)




