from django import forms
from .models import Owner, Patient

class OwnerCreateForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'phone',)

class OwnerUpdateForm(forms.ModelForm):
    #form for updating owners
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'phone',)


