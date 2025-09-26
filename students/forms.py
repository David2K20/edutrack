from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['matric_number', 'first_name', 'last_name', 'email', 'field_of_study', 'cgpa', 'photo']
        labels = {
            'matric_number': 'Matric Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study': 'Field of Study',
            'cgpa': 'CGPA',
            'photo': 'Photo ID'
        }
        widgets = {
            'matric_number': forms.TextInput(attrs = {'class': 'form-control'}),
            'first_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'last_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs = {'class': 'form-control'}),
            'cgpa': forms.NumberInput(attrs = {'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs = {'class': 'form-control-file'}),
        }