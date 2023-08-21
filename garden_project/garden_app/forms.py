from django import forms
from .models import Veisle, Darzo_darbai

class VeisleForm(forms.ModelForm):
    class Meta:
        model = Veisle
        fields = '__all__'

class Darzo_darbaiForm(forms.ModelForm):
    class Meta:
        model = Darzo_darbai
        exclude = ('vartotojas',)