from django import forms
from .models import Veisle, Darzas

class VeisleForm(forms.ModelForm):
    class Meta:
        model = Veisle
        fields = '__all__'

class DarzasForm(forms.ModelForm):
    class Meta:
        model = Darzas
        exclude = ('vartotojas',)