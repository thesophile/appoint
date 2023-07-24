from django.shortcuts import render,redirect
from patients.models import Doctors
from patients.models import Patients

# Create your views here.


def index(request):
    return render(request,'index.html')


def patients(request):

    mydoctor = "mydoctor"

    if request.method=='POST':
        #get values from form
        mydoctor_id = request.POST['selected']
        patient_name = request.POST['patient_name']

        #create patient object
        Patients.objects.create(name=patient_name)
        patient_object = Patients.objects.get(name=patient_name)

        #assign the patient to the selected doctor
        mydoctor_id = int(mydoctor_id)
        mydoctor = Doctors.objects.get(id=mydoctor_id)
        patient_object.doctor.add(mydoctor)

        #get the token number (from the list of patients under the selected doctor)
        patients_qs = mydoctor.patients_set.all()
        patient_list = list(patients_qs)
        token = len(patient_list)
        request.session['token'] = token

        if not len(patient_name)==0:
            return redirect("/patients/success")



    doctor=Doctors.objects.all().values()
    context = {
        'Doctors':doctor,
        'selected_doctor':mydoctor,
    }
        

    return render(request,'patients.html',context)


def success(request):
    token = request.session['token']
    context= {
        'token_no':token
    }
    return render(request,'success.html',context)
