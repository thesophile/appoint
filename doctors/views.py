from django.shortcuts import render,redirect
from patients.models import Doctors
from patients.models import Patients




def doctors(request):

    # Important! patient_diplay should initially be hidden and should only be viewable after
    # entering the correct password
    login_display = "block"
    patient_display = "none"

    #These values should be defined here to prevent 'referenced before assignment error' because
    #these values are called but is not assigned before the submit using request.POST.
    doctor_qs = None
    patient_list = None
    

    # doctor_objects = Doctors.objects.all()

    # doctor_patients= []

    # for doctor_object in doctor_objects:
        
    #     #get the queryset of all patients under a doctor
    #     patients_qs = doctor_object.patients_set.all()
    #     patient_list = list(patients_qs)
    #     doctor_patients.append(patient_list)


    
    #doctor = Doctors.objects.all().values()
    #to get the list of doctors. not used in the below code.
    
    #master_list = zip(doctor_objects, doctor_patients) 

    if request.method=='POST':
        got_username = request.POST['username']
        got_password = request.POST['password']
        doctor_qs = Doctors.objects.get(username=got_username)
        #real_username = doctor_qs.username
        real_password = doctor_qs.password

        #patient_list = doctor_qs.patients_set.all()
        patients_qs = doctor_qs.patients_set.all()
        patient_list = list(patients_qs)
        

        if got_password == real_password:
            patient_display = "block"
            login_display = "none"

    context = {
        'doctor_qs':doctor_qs,
        # 'doctor_objects': doctor_objects,
        'patient_list': patient_list,
        # 'master_list':master_list,
        'patient_display':patient_display,
        'login_display':login_display,
    }
        
    return render(request,'doctors.html',context)




