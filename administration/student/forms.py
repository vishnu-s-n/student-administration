from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'physics_marks', 'chemistry_marks', 'maths_marks', 'computer_science_marks']


        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            'date_of_birth': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            'physics_marks': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            'chemistry_marks': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            'maths_marks': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            'computer_science_marks': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
        }