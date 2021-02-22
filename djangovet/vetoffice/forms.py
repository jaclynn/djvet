from django import forms
from .models import Owner, Patient

class OwnerCreateForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'phone',)

class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('pet_name', 'animal_type', 'breed', 'age', 'owner')

class OwnerUpdateForm(forms.ModelForm):
    #form for updating owners
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'phone',)

class PatientUpdateForm(forms.ModelForm):
    #form for updating patients
    class Meta:
        model = Patient
        fields = ('pet_name', 'animal_type', 'breed', 'age', 'owner')