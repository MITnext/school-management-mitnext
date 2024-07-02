from django.db import models


# Create your models here.

class MasterEmployeeType(models.Model):
    employee_type_id = models.CharField(max_length=2, unique=True)
    employee_type = models.CharField(max_length=15, primary_key=True, unique=True)

    def __str__(self):
        return self.employee_type


class Employee(models.Model):
    employee_id = models.CharField(max_length=10)
    name = models.CharField(max_length=80)
    phone_no = models.IntegerField(unique=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=350)
    qualification = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    marital_status = models.CharField(max_length=10)
    father_or_husband = models.CharField(max_length=80)
    experience = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5, null=True)
    aadhar = models.IntegerField(null=True)
    pan = models.CharField(max_length=10, null=True)
    type = models.ForeignKey(MasterEmployeeType, on_delete=models.CASCADE)
    leaving_date = models.DateField(null=True)
    leaving_reason = models.CharField(max_length=80, null=True)
    photo = models.FileField(null=True)
    salary = models.IntegerField(null=True)

    def __str__(self):
        return self.employee_id


""" Created Exam models by Kunal D"""


class subjectmaster(models.Model):
    subjectname = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.subjectname


class questionbank(models.Model):
    MCQ = 'MCQ'
    SUBJECTIVE = 'Subjective'
    QUESTION_TYPES = [
        (MCQ, 'Multiple Choice Question'),
        (SUBJECTIVE, 'Subjective Question'),
    ]

    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    subject = models.ForeignKey(subjectmaster, on_delete=models.CASCADE)
    question = models.CharField(max_length=3000)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    option1 = models.CharField(max_length=200, null=True, blank=True)
    option2 = models.CharField(max_length=200, null=True, blank=True)
    option3 = models.CharField(max_length=200, null=True, blank=True)
    option4 = models.CharField(max_length=200, null=True, blank=True)
    solution = models.CharField(max_length=3000)
    option_choices_type = [
        ('option1', 'Option1'),
        ('option2', 'Option2'),
        ('option3', 'Option3'),
        ('option4', 'Option4'),
    ]
    option_choices = models.CharField('Option Type', max_length=10, blank=False, choices=option_choices_type)
    question_weightage_type = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]
    question_weightage = models.IntegerField(default=1, choices=question_weightage_type)
