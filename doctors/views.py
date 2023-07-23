from django.shortcuts import render,redirect
from patients.models import Doctors
from patients.models import Patients

# Create your views here.





def doctors(request):

    login_display = "block"
    patient_display = "none"

    doctor_objects = Doctors.objects.all()

    doctor_patients= []

    for doctor_object in doctor_objects:
        
        #get the queryset of all patients under a doctor
        patients_qs = doctor_object.patients_set.all()
        patient_list = list(patients_qs)
        doctor_patients.append(patient_list)


    
    doctor = Doctors.objects.all().values()
    
    master_list = zip(doctor_objects, doctor_patients) 

    if request.method=='POST':
        username = request.POST['username']
        if not len(username)==0:
            patient_display = "block"
            login_display = "none"

    context = {
        'doctor_objects': doctor_objects,
        'doctor_patients': doctor_patients,
        'master_list':master_list,
        'patient_display':patient_display,
        'login_display':login_display,
    }
        
    return render(request,'doctors.html',context)




