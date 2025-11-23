from django import forms
from .models import Employee , Project


class PostForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'date_joined', 'date_of_birth' , 'position', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'date_joined': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'position': forms.TextInput(attrs={'placeholder': 'Enter position'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter department'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['employee', 'name', 'start_date', 'end_date', 'amount']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
        }