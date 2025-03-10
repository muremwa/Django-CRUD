from django import forms
from .models import Employee
from bootstrap_modal_forms.forms import BSModalModelForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EmployeeModelForm(BSModalModelForm):
    class Meta:
        model = Employee
        fields = ('ID', 'Date_of_Employement', 'Name', 'Email', 'Phone_Number', 'Job')
