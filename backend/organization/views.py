from django.shortcuts import render, get_object_or_404, redirect
from .models import Organization
from .serializers import OrganizationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import OrganizationForm
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone
from twilio.rest.frontline_api.v1 import user
from .models import Profile
from .forms import RegistrationForm, LoginForm, OTPForm, StudentRegistrationForm
from twilio.rest import Client
from datetime import timedelta, datetime
import random


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            otp, otp_expiration = generate_otp()
            send_otp_sms(user.phone_number, otp)
            request.session['otp'] = otp
            request.session['otp_expiration'] = otp_expiration.isoformat()
            request.session['phone_number'] = user.phone_number
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('validate_otp')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                otp, otp_expiration = generate_otp()
                send_otp_sms(user.phone_number, otp)
                request.session['otp'] = otp
                request.session['otp_expiration'] = otp_expiration.isoformat()
                request.session['phone_number'] = user.phone_number
                request.session['login_user_id'] = user.id
                return redirect('validate_otp_login')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def validate_otp_login(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            stored_otp = request.session.get('otp')
            stored_otp_expiration = datetime.fromisoformat(request.session.get('otp_expiration'))
            if otp == stored_otp and stored_otp_expiration > timezone.now():
                user_id = request.session.get('login_user_id')
                user = Profile.objects.get(id=user_id)
                login(request, user)
                # Clear session data after successful validation
                del request.session['otp']
                del request.session['otp_expiration']
                del request.session['phone_number']
                del request.session['login_user_id']
                return redirect_user_based_on_role(user)
            else:
                return render(request, 'validate_otp.html', {'form': form, 'error': 'Invalid or expired OTP'})
    else:
        form = OTPForm()
    return render(request, 'validate_otp.html', {'form': form})


def generate_otp():
    otp = str(random.randint(100000, 999999))
    otp_expiration = timezone.now() + timedelta(minutes=15)
    return otp, otp_expiration




def validate_otp(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            stored_otp = request.session.get('otp')
            stored_otp_expiration = datetime.fromisoformat(request.session.get('otp_expiration'))
            if otp == stored_otp and stored_otp_expiration > timezone.now():
                # Fetch the user associated with the validated phone number
                phone_number = request.session.get('phone_number')
                try:
                    user = Profile.objects.get(phone_number=phone_number)
                except Profile.MultipleObjectsReturned:
                    # Handle the case where multiple users have the same phone number
                    users = Profile.objects.filter(phone_number=phone_number)
                    # Decide how to handle this case, for example, pick the first one
                    user = users.first()

                # Log in the user
                login(request, user)

                # Clear session data
                del request.session['otp']
                del request.session['otp_expiration']
                del request.session['phone_number']

                # Redirect based on user role
                return redirect_user_based_on_role(user)
            else:
                return render(request, 'validate_otp.html', {'form': form, 'error': 'Invalid or expired OTP'})
    else:
        form = OTPForm()
    return render(request, 'validate_otp.html', {'form': form})


def redirect_user_based_on_role(user):
    if user.role == 'Student':
        return redirect('student_dashboard')
    elif user.role == 'Teacher':
        return redirect('teacher_dashboard')
    elif user.role == 'Principal':
        return redirect('principal_dashboard')
    else:
        return redirect('login')


def user_logout(request):
    logout(request)
    return redirect('login')


def student_dashboard(request):
    return render(request, 'student_dashboard.html')


def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')


def principal_dashboard(request):
    return render(request, 'principal_dashboard.html')


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            otp, otp_expiration = generate_otp()
            send_otp_sms(student.phone_number, otp)
            request.session['otp'] = otp
            request.session['otp_expiration'] = otp_expiration.isoformat()
            request.session['phone_number'] = student.phone_number
            student.save()
            return redirect('validate_otp')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})


@api_view(['GET'])
def organization_list(request):
    organizations = Organization.objects.all()
    serializer = OrganizationSerializer(organizations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    serializer = OrganizationSerializer(organization, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_organization(request):
    serializer = OrganizationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    serializer = OrganizationSerializer(organization, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    organization.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def add_organization(request):
    my_dict = {}
    form = OrganizationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_organizations')

    return render(request, 'add_organization.html')


def list_organizations(request):
    organizations = Organization.objects.all()
    return render(request, 'organization_list.html', {'organizations': organizations})
