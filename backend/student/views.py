from django.contrib import messages
from django.template.loader import get_template
from rest_framework.decorators import api_view
from rest_framework.views import Response
from .models import *
from .serializers import *
from rest_framework import serializers, status
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework.response import Response

""" Section_Views """


def section_create(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm()
    return render(request, 'section_class/section_create.html', {'form': form})


def section_list(request):
    sections = Section_master.objects.all()
    return render(request, 'section_class/section_list.html', {'sections': sections})


def section_detail(request, pk):
    section = get_object_or_404(Section_master, pk=pk)
    return render(request, 'section_class/section_detail.html', {'section': section})


def section_update(request, pk):
    section = get_object_or_404(Section_master, pk=pk)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm(instance=section)
    return render(request, 'section_class/section_update.html', {'form': form})


def section_delete(request, pk):
    section = get_object_or_404(Section_master, pk=pk)
    if request.method == 'POST':
        section.delete()
        return redirect('section_list')
    return render(request, 'section_class/section_delete.html', {'section': section})


""" Section_apis """


@api_view(['POST'])
def section_create_api(request):
    section = SectionSerializer(data=request.data)
    if section.is_valid():
        section.save()
        return Response(section.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def section_search_byid_api(request, pk):
    section = Section_master.objects.filter(pk=pk)
    if section:
        serializer = SectionSerializer(section, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def section_search_api(request):
    section = Section_master.objects.all()
    if section:
        serializer = SectionSerializer(section, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def section_update_api(request, pk):
    section = Section_master.objects.get(pk=pk)
    serializer = SectionSerializer(instance=section, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def section_delete_api(request, pk):
    section = get_object_or_404(Section_master, pk=pk)
    section.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


"""**************************************************************************************************************************************************** 
 # ****************************************************************************************************************************************************"""

"""StdClass Views"""


def std_class_create(request):
    if request.method == 'POST':
        form = StdClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('std_class_list')
    else:
        form = StdClassForm()
    return render(request, 'section_class/std_class_create.html', {'form': form})


def std_class_list(request):
    classes = StdClass_master.objects.all()
    return render(request, 'section_class/std_class_list.html', {'classes': classes})


def std_class_detail(request, pk):
    std_class = get_object_or_404(StdClass_master, pk=pk)
    return render(request, 'section_class/std_class_detail.html', {'std_class': std_class})


def std_class_update(request, pk):
    std_class = get_object_or_404(StdClass_master, pk=pk)
    if request.method == 'POST':
        form = StdClassForm(request.POST, instance=std_class)
        if form.is_valid():
            form.save()
            return redirect('std_class_list')
    else:
        form = StdClassForm(instance=std_class)
    return render(request, 'section_class/std_class_update.html', {'form': form})


def std_class_delete(request, pk):
    std_class = get_object_or_404(StdClass_master, pk=pk)
    if request.method == 'POST':
        std_class.delete()
        return redirect('std_class_list')
    return render(request, 'section_class/std_class_delete.html', {'std_class': std_class})


"""StdClass APIs"""


@api_view(['POST'])
def stdclass_create_api(request):
    stdclass = StdClassSerializer(data=request.data)
    if stdclass.is_valid():
        stdclass.save()
        return Response(stdclass.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def stdclass_search_byid_api(request, pk):
    stdclass = StdClass_master.objects.filter(pk=pk)
    if stdclass:
        serializer = StdClassSerializer(stdclass, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def stdclass_search_api(request):
    stdclass = StdClass_master.objects.all()
    if stdclass:
        serializer = StdClassSerializer(stdclass, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def stdclass_update_api(request, pk):
    stdclass = StdClass_master.objects.get(pk=pk)
    serializer = StdClassSerializer(instance=stdclass, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def stdclass_delete_api(request, pk):
    stdclass = get_object_or_404(StdClass_master, pk=pk)
    stdclass.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


""" ****************************************************************************************************************************************************
# **************************************************************************************************************************************************** """

"""Religion Views"""


def religion_create(request):
    if request.method == 'POST':
        form = ReligionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('religion_list')
    else:
        form = ReligionForm()
    return render(request, 'Religion_caste/religion_create.html', {'form': form})


def religion_list(request):
    religions = Religion_master.objects.all()
    return render(request, 'Religion_caste/religion_list.html', {'religions': religions})


def religion_detail(request, pk):
    religion = get_object_or_404(Religion_master, pk=pk)
    return render(request, 'Religion_caste/religion_detail.html', {'religion': religion})


def religion_update(request, pk):
    religion = get_object_or_404(Religion_master, pk=pk)
    if request.method == 'POST':
        form = ReligionForm(request.POST, instance=religion)
        if form.is_valid():
            form.save()
            return redirect('religion_list')
    else:
        form = ReligionForm(instance=religion)
    return render(request, 'Religion_caste/religion_form.html', {'form': form})


def religion_delete(request, pk):
    religion = get_object_or_404(Religion_master, pk=pk)
    if request.method == 'POST':
        religion.delete()
        return redirect('religion_list')
    return render(request, 'Religion_caste/religion_delete.html', {'religion': religion})


""" Religion APIs """


@api_view(['POST'])
def religion_create_api(request):
    state = ReligionSerializer(data=request.data)
    if state.is_valid():
        state.save()
        return Response(state.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def religion_search_byid_api(request, pk):
    religion = Religion_master.objects.filter(pk=pk)
    if religion:
        serializer = ReligionSerializer(religion, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def religion_search_api(request):
    religion = Religion_master.objects.all()
    if religion:
        serializer = ReligionSerializer(religion, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def religion_update_api(request, pk):
    religion = Religion_master.objects.get(pk=pk)
    serializer = ReligionSerializer(instance=religion, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def religion_delete_api(request, pk):
    religion = get_object_or_404(Religion_master, pk=pk)
    religion.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


""" ****************************************************************************************************************************************************
# **************************************************************************************************************************************************** """

""" Main Caste views """


def maincaste_create(request):
    if request.method == 'POST':
        form = MainCasteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('casteMain_list')
    else:
        form = MainCasteForm()
    return render(request, 'Religion_caste/maincaste_create.html', {'form': form})


def maincaste_list(request):
    castes = MainCaste_master.objects.all()
    return render(request, 'Religion_caste/maincaste_list.html', {'castes': castes})


def maincaste_detail(request, pk):
    caste = get_object_or_404(MainCaste_master, pk=pk)
    return render(request, 'Religion_caste/maincaste_detail.html', {'caste': caste})


def maincaste_update(request, pk):
    caste = get_object_or_404(MainCaste_master, pk=pk)
    if request.method == 'POST':
        form = MainCasteForm(request.POST, instance=caste)
        if form.is_valid():
            form.save()
            return redirect('casteMain_list')
    else:
        form = MainCasteForm(instance=caste)
    return render(request, 'Religion_caste/maincaste_form.html', {'form': form})


def maincaste_delete(request, pk):
    caste = get_object_or_404(MainCaste_master, pk=pk)
    if request.method == 'POST':
        caste.delete()
        return redirect('casteMain_list')
    return render(request, 'Religion_caste/maincaste_delete.html', {'caste': caste})


""" Main_caste APIs """


@api_view(['POST'])
def maincaste_create_api(request):
    maincaste = MainCaste_master(data=request.data)
    if maincaste.is_valid():
        maincaste.save()
        return Response(maincaste.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def maincaste_search_byid_api(request, pk):
    maincaste = MainCaste_master.objects.filter(pk=pk)
    if maincaste:
        serializer = MainCasteSerializer(maincaste, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def maincaste_search_api(request):
    maincaste = MainCaste_master.objects.all()
    if maincaste:
        serializer = MainCasteSerializer(maincaste, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def maincaste_update_api(request, pk):
    maincaste = MainCaste_master.objects.get(pk=pk)
    serializer = MainCasteSerializer(instance=maincaste, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def maincaste_delete_api(request, pk):
    maincaste = get_object_or_404(MainCaste_master, pk=pk)
    maincaste.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


""" ****************************************************************************************************************************************************
# ****************************************************************************************************************************************************  """

""" Sub caste views"""


def subcaste_create(request):
    if request.method == 'POST':
        form = SubCasteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('casteSub_list')
    else:
        form = SubCasteForm()
    return render(request, 'Religion_caste/subcaste_create.html', {'form': form})


def subcaste_list(request):
    castes = SubCaste_master.objects.all()
    return render(request, 'Religion_caste/subcaste_list.html', {'castes': castes})


def subcaste_detail(request, pk):
    caste = get_object_or_404(SubCaste_master, pk=pk)
    return render(request, 'Religion_caste/subcaste_detail.html', {'caste': caste})


def subcaste_update(request, pk):
    caste = get_object_or_404(SubCaste_master, pk=pk)
    if request.method == 'POST':
        form = SubCasteForm(request.POST, instance=caste)
        if form.is_valid():
            form.save()
            return redirect('casteSub_list')
    else:
        form = SubCasteForm(instance=caste)
    return render(request, 'Religion_caste/subcaste_form.html', {'form': form})


def subcaste_delete(request, pk):
    caste = get_object_or_404(SubCaste_master, pk=pk)
    if request.method == 'POST':
        caste.delete()
        return redirect('casteSub_list')
    return render(request, 'Religion_caste/subcaste_delete.html', {'caste': caste})


""" Sub Caste APIs """


@api_view(['POST'])
def subcaste_create_api(request):
    subcaste = SubCasteSerializer(data=request.data)
    if subcaste.is_valid():
        subcaste.save()
        return Response(subcaste.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def subcaste_search_byid_api(request, pk):
    subcaste = SubCaste_master.objects.filter(pk=pk)
    if subcaste:
        serializer = SubCasteSerializer(subcaste, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def subcaste_search_api(request):
    subcaste = SubCaste_master.objects.all()
    if subcaste:
        serializer = SubCasteSerializer(subcaste, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def subcaste_update_api(request, pk):
    subcaste = SubCaste_master.objects.get(pk=pk)
    serializer = SubCasteSerializer(instance=subcaste, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def subcaste_delete_api(request, pk):
    subcaste = get_object_or_404(SubCaste_master, pk=pk)
    subcaste.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


""" ****************************************************************************************************************************************************
# **************************************************************************************************************************************************** """

""" State views """


def state_create(request):
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('added successfully')
    else:
        form = StateForm()
    return render(request, 'state_city/state_create.html', {'form': form})


def search_state(request):
    sal = State_master.objects.all()
    return render(request, "state_city/search_state.html", {'subm': sal})


def update_state(request, pk):
    branch = State_master.objects.get(pk=pk)
    form = StateForm(initial={'statename': branch.state_name, 'stateshortcut': branch.state_shortcut, })
    if request.method == "POST":
        form = StateForm(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/search_state')
            except Exception as e:
                pass
    return render(request, 'state_city/update_state.html', {'form': form})


def delete_state(request, pk):
    state = State_master.objects.get(pk=pk)
    try:
        state.delete()
    except:
        pass
    return redirect('/search_state')


""" State APIs """


@api_view(['POST'])
def state_create_api(request):
    state = StateSerializer(data=request.data)
    if state.is_valid():
        state.save()
        return Response(state.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def state_search_api(request):
    states = State_master.objects.all()
    if states:
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def state_update_api(request, pk):
    states = State_master.objects.get(pk=pk)
    serializer = StateSerializer(instance=states, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def state_delete_api(request, pk):
    states = get_object_or_404(State_master, pk=pk)
    states.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


"""# ****************************************************************************************************************************************************
# **************************************************************************************************************************************************** """

""" City views """


def city_create(request):
    context = {}
    statenames = State_master.objects.all()
    employee = CityForm(request.POST or None)
    if employee.is_valid():
        print("HELOO______________________________________________________")
        employee.save()
    else:
        print("HELOO______________________________________________________111")
        print(request.POST)
        messages.error(request, employee.errors)
        context['form'] = employee

    context["statenames"] = statenames
    return render(request, "state_city/city_create.html", context)


def search_city(request):
    sal = City_master.objects.all()
    return render(request, "state_city/search_city.html", {'subm': sal})


def update_city(request, pk):
    branch = City_master.objects.get(pk=pk)
    form = CityForm(
        initial={'state': branch.state, 'cityname': branch.city_name, 'cityshortcut': branch.city_shortcut, })
    if request.method == "POST":
        form = CityForm(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/search_city')
            except Exception as e:
                pass
    return render(request, 'state_city/update_city.html', {'form': form})


def delete_city(request, pk):
    city = City_master.objects.get(pk=pk)
    try:
        city.delete()
    except:
        pass
    return redirect('/search_city')


""" city APIs """


@api_view(['POST'])
def city_create_api(request):
    city = citySerializer(data=request.data)
    if city.is_valid():
        city.save()
        return Response(city.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def city_search_api(request):
    cities = City_master.objects.all()
    if cities:
        serializer = citySerializer(cities, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def city_update_api(request, pk):
    cities = City_master.objects.get(pk=pk)
    serializer = citySerializer(instance=cities, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def city_delete_api(request, pk):
    cities = get_object_or_404(City_master, pk=pk)
    cities.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


"""# ****************************************************************************************************************************************************
# ****************************************************************************************************************************************************  """

""" student views """


def student_create(request):
    if request.method == 'POST':
        form = StudentPersonalDetailsForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('added successfully')
    else:
        form = StudentPersonalDetailsForm()
        messages.error(request, form.errors)
        print(form)
        print(form.is_valid())
    return render(request, 'Details/student_create.html', {'form': form})


def student_search(request):
    sal = StudentPersonalDetails.objects.all()
    return render(request, "Details/student_search.html", {'subm': sal})


def student_update(request, std_id):
    branch = get_object_or_404(StudentPersonalDetails, std_id=std_id)
    form = StudentPersonalDetailsForm(instance=branch)
    if request.method == "POST":
        form = StudentPersonalDetailsForm(request.POST, request.FILES, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('/student_search')
    return render(request, 'Details/student_update.html', {'form': form})


# def student_update(request, student_id):
#     branch = StudentPersonalDetails.objects.get(student_id=student_id)
#     form = StudentPersonalDetailsForm(initial={'statename': branch.statename, 'studenthortcut': branch.studenthortcut, })
#     if request.method == "POST":
#         form = StudentPersonalDetailsForm(request.POST, instance=branch)
#         if form.is_valid():
#             try:
#                 form.save()
#                 model = form.instance
#                 return redirect('/student_search')
#             except Exception as e:
#                 pass
#     return render(request, 'student_update.html', {'form': form})


def student_delete(request, std_id):
    state = StudentPersonalDetails.objects.get(std_id=std_id)
    try:
        state.delete()
    except:
        pass
    return redirect('/student_search')


"""# ****************************************************************************************************************************************************
# **************************************************************************************************************************************************** """


# def previous_school_create(request):
#     if request.method == 'POST':
#         form = PreviousSchoolDetailsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Added successfully')
#     else:
#         form = PreviousSchoolDetailsForm()
#     return render(request, 'previous_school_create.html', {'form': form})


def previous_school_create(request):
    context = {}
    stdname = StudentPersonalDetails.objects.all()
    form = PreviousSchoolDetailsForm(request.POST or None)
    if form.is_valid():
        print("HELOO______________________________________________________")
        form.save()
    else:
        print("HELOO______________________________________________________111")
        print(request.POST)
        messages.error(request, form.errors)
        context['form'] = form

    context["stdname"] = stdname
    return render(request, "Details/previous_school_create.html", context)


def previous_school_search(request):
    schools = PreviousSchoolDetails.objects.all()
    return render(request, "Details/previous_school_search.html", {'schools': schools})


def previous_school_update(request, pk):
    school = get_object_or_404(PreviousSchoolDetails, pk=pk)
    form = PreviousSchoolDetailsForm(instance=school)
    if request.method == "POST":
        form = PreviousSchoolDetailsForm(request.POST, request.FILES, instance=school)
        if form.is_valid():
            form.save()
            return redirect('/previous_school_search')
    return render(request, 'Details/previous_school_update.html', {'form': form})


def previous_school_delete(request, pk):
    school = get_object_or_404(PreviousSchoolDetails, pk=pk)
    school.delete()
    return redirect('/previous_school_search')


# ****************************************************************************************************************************************************
# ****************************************************************************************************************************************************
# ****************************************************************************************************************************************************
# ****************************************************************************************************************************************************

""" Student personal details APIs """


@api_view(['POST'])
def student_create_api(request):
    state = StudentPersonalDetailsSerializer(data=request.data)
    if state.is_valid():
        state.save()
        return Response(state.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def student_search_byid_api(request, pk):
    student = StudentPersonalDetails.objects.filter(pk=pk)
    if student:
        serializer = StudentPersonalDetailsSerializer(student, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def student_search_api(request):
    student = StudentPersonalDetails.objects.all()
    if student:
        serializer = StudentPersonalDetailsSerializer(student, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def student_update_api(request, pk):
    student = StudentPersonalDetails.objects.get(pk=pk)
    serializer = StudentPersonalDetailsSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete_api(request, pk):
    student = get_object_or_404(StudentPersonalDetails, pk=pk)
    student.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


"""# ****************************************************************************************************************************************************
# **************************************************************************************************************************************************** """

"""previous_school APIs """ 


@api_view(['POST'])
def previous_school_create_api(request):
    serializer = PreviousSchoolDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def previous_school_search_byid_api(request, pk):
    school = get_object_or_404(PreviousSchoolDetails, pk=pk)
    serializer = PreviousSchoolDetailsSerializer(school)
    return Response(serializer.data)


@api_view(['GET'])
def previous_school_search_api(request):
    schools = PreviousSchoolDetails.objects.all()
    serializer = PreviousSchoolDetailsSerializer(schools, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def previous_school_update_api(request, pk):
    school = get_object_or_404(PreviousSchoolDetails, pk=pk)
    serializer = PreviousSchoolDetailsSerializer(instance=school, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def previous_school_delete_api(request, pk):
    school = get_object_or_404(PreviousSchoolDetails, pk=pk)
    school.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
