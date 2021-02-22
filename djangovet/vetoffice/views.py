from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Owner
from .forms import OwnerCreateForm, OwnerUpdateForm

# Create your views here.
def home(request):
   context = {"name": "<Put your name here>"}
   return render(request, 'vetoffice/home.html', context)

# CRUD - (R)ead
class OwnerList(ListView):
   model = Owner

# CRUD - (C)reate
class OwnerCreate(CreateView):
   model = Owner
   template_name = 'vetoffice/owner_create_form.html'
   form_class = OwnerCreateForm

# CRUD - (U)pdate
class OwnerUpdate(UpdateView):
   model = Owner
   template_name = 'vetoffice/owner_update_form.html'
   form_class = OwnerUpdateForm

# CRUD - (D)elete
class OwnerDelete(DeleteView):
    model = Owner
    template_name = 'vetoffice/owner_delete_form.html'
    success_url = '/owner/list'

