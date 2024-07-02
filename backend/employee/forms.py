from django import forms
from .models import *


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    type = forms.ModelChoiceField(queryset=MasterEmployeeType.objects.all(), empty_label="Select Employee Type")


""" Created Exam forms by Kunal D"""


class subjectmasterform(forms.ModelForm):
    class Meta:
        model = subjectmaster
        fields = ['subjectname', 'description']


class mcqqueform(forms.ModelForm):
    class Meta:
        model = questionbank
        fields = ["question_type", "subject", "question", "image", "option1", "option2", "option3", "option4",
                  "option_choices", ]


class subjectivequeform(forms.ModelForm):
    class Meta:
        model = questionbank
        fields = ["question_type", "subject", "question", "image", "solution", "question_weightage", ]
