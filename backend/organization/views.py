from django.shortcuts import render, get_object_or_404, redirect
from .models import Organization
from .serializers import OrganizationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import OrganizationForm


# Create your views here.
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
