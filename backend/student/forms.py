# forms.py
from django import forms
from .models import *


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section_master
        fields = '__all__'


class StdClassForm(forms.ModelForm):
    class Meta:
        model = StdClass_master
        fields = '__all__'


class ReligionForm(forms.ModelForm):
    class Meta:
        model = Religion_master
        fields = '__all__'


class MainCasteForm(forms.ModelForm):
    class Meta:
        model = MainCaste_master
        fields = '__all__'


class SubCasteForm(forms.ModelForm):
    class Meta:
        model = SubCaste_master
        fields = '__all__'


class StateForm(forms.ModelForm):
    class Meta:
        model = State_master
        fields = '__all__'


class CityForm(forms.ModelForm):
    class Meta:
        model = City_master
        fields = '__all__'


class StudentPersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentPersonalDetails
        fields = '__all__'


class PreviousSchoolDetailsForm(forms.ModelForm):
    class Meta:
        model = PreviousSchoolDetails
        fields = '__all__'
