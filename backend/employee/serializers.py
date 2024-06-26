from rest_framework import serializers
from .models import Employee, MasterEmployeeType

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
class EmployeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterEmployeeType
        fields = '__all__'
        