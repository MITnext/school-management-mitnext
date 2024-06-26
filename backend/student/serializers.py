# serializers.py
from rest_framework import serializers
from .models import *


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section_master
        fields = "__all__"


class StdClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StdClass_master
        fields = "__all__"


class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion_master
        fields = "__all__"


class MainCasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCaste_master
        fields = "__all__"


class SubCasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCaste_master
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State_master
        fields = "__all__"


class citySerializer(serializers.ModelSerializer):
    class Meta:
        model = City_master
        fields = "__all__"


class StudentPersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPersonalDetails
        fields = '__all__'


class PreviousSchoolDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousSchoolDetails
        fields = '__all__'
