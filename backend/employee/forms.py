from django import forms
from .models import Employee, MasterEmployeeType

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
    type = forms.ModelChoiceField(queryset=MasterEmployeeType.objects.all(), empty_label="Select Employee Type")
