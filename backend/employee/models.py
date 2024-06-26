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
    
    