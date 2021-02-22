from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Owner, Patient
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm

# Create your views here.
def home(request):
   context = {"name": "<Put your name here>"}
   return render(request, 'vetoffice/home.html', context)

# CRUD - (R)ead
class OwnerList(ListView):
   model = Owner

class PatientList(ListView):
    model = Patient

# CRUD - (C)reate
class OwnerCreate(CreateView):
   model = Owner
   template_name = 'vetoffice/owner_create_form.html'
   form_class = OwnerCreateForm

class PatientCreate(CreateView):
    model=Patient
    template_name = 'vetoffice/patient_create_form.html'
    form_class = PatientCreateForm

# CRUD - (U)pdate
class OwnerUpdate(UpdateView):
   model = Owner
   template_name = 'vetoffice/owner_update_form.html'
   form_class = OwnerUpdateForm

class PatientUpdate(UpdateView):
   model = Patient
   template_name = 'vetoffice/patient_update_form.html'
   form_class = PatientUpdateForm

# CRUD - (D)elete
class OwnerDelete(DeleteView):
    model = Owner
    template_name = 'vetoffice/owner_delete_form.html'
    success_url = '/owner/list'

class PatientDelete(DeleteView):
    model = Patient
    template_name = 'vetoffice/patient_delete_form.html'
    success_url = '/patient/list'
