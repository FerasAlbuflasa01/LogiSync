from django.forms import ModelForm
from django import forms
from .models import Package, Profile

class PackageForm(ModelForm):
    class Meta:
        model=Package
        fields='__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role', 'phone']