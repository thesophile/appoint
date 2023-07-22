from django.shortcuts import render
from patients.models import Doctors
from patients.models import Patients

# Create your views here.


def index(request):
    return render(request,'index.html')


def patients(request):

    mydoctor = "mydoctor"

    if request.method=='POST':
        selected_doctor = request.POST['selected']
        patient_name = request.POST['patient_name']
        Patients.objects.create(name=patient_name)
        patient_object = Patients.objects.last()

        selected_doctor = int(selected_doctor)
        mydoctor = Doctors.objects.all()[selected_doctor-1]
        patient_object.doctor.add(mydoctor)

    doctor=Doctors.objects.all().values()
    context = {
        'Doctors':doctor,
        'selected_doctor':mydoctor,
    }
        

    return render(request,'patients.html',context)


