from django.shortcuts import render
from django.http import HttpResponse 
from .models import Department,Doctors
from .forms import Bookingform

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == 'POST':
        form = Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
   
    form = Bookingform()    
    dict_form = {
        'form': form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)
def contacts(request):
    return render(request,'contacts.html')

def departments(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request,'departments.html',dict_dept)
