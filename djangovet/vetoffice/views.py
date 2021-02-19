from django.shortcuts import render
from django.views.generic import ListView

from .models import Owner

pets = [
   { 'petname': 'Fido', 'animal_type': 'dog'},
   { 'petname': 'Clementine', 'animal_type': 'cat'},
   { 'petname': 'Cleo', 'animal_type': 'cat'},
   { 'petname': 'Oreo', 'animal_type': 'dog'},
]

# Create your views here.
def home(request):
   context = {"name": "<Put your name here>", "pets": pets}
   return render(request, 'vetoffice/home.html', context)

class OwnerList(ListView):
   model = Owner
