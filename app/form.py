from django import forms
 
class Student_regisition(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()