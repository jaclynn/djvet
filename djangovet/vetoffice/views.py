from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Owner, Patient
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm

# Create your views here.
@login_required
def home(request):
   context = {"name": "<Put your name here>"}
   return render(request, 'vetoffice/home.html', context)

# CRUD - (R)ead
class OwnerList(LoginRequiredMixin, ListView):
   model = Owner

class PatientList(LoginRequiredMixin, ListView):
    model = Patient

# CRUD - (C)reate
class OwnerCreate(LoginRequiredMixin, CreateView):
   model = Owner
   template_name = 'vetoffice/owner_create_form.html'
   form_class = OwnerCreateForm

class PatientCreate(LoginRequiredMixin, CreateView):
    model=Patient
    template_name = 'vetoffice/patient_create_form.html'
    form_class = PatientCreateForm

# CRUD - (U)pdate
class OwnerUpdate(LoginRequiredMixin, UpdateView):
   model = Owner
   template_name = 'vetoffice/owner_update_form.html'
   form_class = OwnerUpdateForm

class PatientUpdate(LoginRequiredMixin, UpdateView):
   model = Patient
   template_name = 'vetoffice/patient_update_form.html'
   form_class = PatientUpdateForm

# CRUD - (D)elete
class OwnerDelete(LoginRequiredMixin, DeleteView):
    model = Owner
    template_name = 'vetoffice/owner_delete_form.html'
    success_url = '/owner/list'

class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = 'vetoffice/patient_delete_form.html'
    success_url = '/patient/list'
