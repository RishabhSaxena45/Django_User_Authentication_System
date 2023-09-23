from django import forms

class studentform(forms.Form):
    name = forms.CharField(max_length=20)
    age = forms.IntegerField()
    course = forms.CharField(max_length=10)