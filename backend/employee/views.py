from django.shortcuts import render, get_object_or_404,redirect
from .models import Employee, MasterEmployeeType
from .serializers import EmployeeSerializer, EmployeeTypeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import EmployeeForm


"""Views for Employee Table"""

@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_employee(request, pk):
    employee =  get_object_or_404(Employee, pk=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])  
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_employees')
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})

def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


"""Views for Master Table Employee Type"""

@api_view(['GET'])
def employee_type_list(request):
    employee_type = MasterEmployeeType.objects.all()
    serializer = EmployeeTypeSerializer(employee_type, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_employee_type(request, pk):
    employee_type = get_object_or_404(MasterEmployeeType, pk=pk)
    serializer = EmployeeTypeSerializer(employee_type, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_employee_type(request):
    serializer = EmployeeTypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_employee_type(request, pk):
    employee_type = get_object_or_404(MasterEmployeeType, pk=pk)
    serializer = EmployeeTypeSerializer(employee_type, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_employee_type(request, pk):
    employee_type = get_object_or_404(MasterEmployeeType, pk=pk)
    employee_type.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
