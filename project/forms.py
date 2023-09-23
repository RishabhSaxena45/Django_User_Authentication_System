from django import forms
from .models import filedetails

class fileform(forms.ModelForm):
    class Meta:
        model = filedetails
        fields = ['name' , 'file']
   