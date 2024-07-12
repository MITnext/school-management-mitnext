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

""" Section Views """


def section_create(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/search_section')
    else:
        form = SectionForm()
    return render(request, 'section_class/section_create.html', {'form': form})


def search_section(request):
    sections = Section_master.objects.all()
    return render(request, "section_class/search_section.html", {'sections': sections})


def update_section(request, id):
    section = get_object_or_404(Section_master, id=id)
    form = SectionForm(instance=section)

    if request.method == "POST":
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search_section')
            except Exception as e:
                pass

    return render(request, 'section_class/update_section.html', {'form': form})


def delete_section(request, id):
    section = get_object_or_404(Section_master, id=id)
    try:
        section.delete()
    except Exception as e:
        pass
    return redirect('/search_section')


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
    context = {}
    sections = Section_master.objects.all()
    stdclass = StdClassForm(request.POST)
    if stdclass.is_valid():
        stdclass.save()
        return redirect('/search_stdclass')
    else:
        context['form'] = stdclass

    context["sections"] = sections
    return render(request, "section_class/std_class_create.html", context)


def search_stdclass(request):
    stdclasses = StdClass_master.objects.all()
    return render(request, "section_class/search_stdclass.html", {'stdclasses': stdclasses})


def update_stdclass(request, id):
    stdclass = get_object_or_404(StdClass_master, id=id)
    form = StdClassForm(instance=stdclass)

    if request.method == "POST":
        form = StdClassForm(request.POST, instance=stdclass)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search_stdclass')
            except Exception as e:
                pass

    return render(request, 'section_class/update_stdclass.html', {'form': form})


def delete_stdclass(request, id):
    stdclass = get_object_or_404(StdClass_master, id=id)
    try:
        stdclass.delete()
    except Exception as e:
        pass
    return redirect('/search_stdclass')


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
            return redirect('/search_religion')
    else:
        form = ReligionForm()
    return render(request, 'Religion_caste/religion_create.html', {'form': form})


def search_religion(request):
    religions = Religion_master.objects.all()
    return render(request, "Religion_caste/search_religion.html", {'religions': religions})


def update_religion(request, id):
    religion = get_object_or_404(Religion_master, id=id)
    form = ReligionForm(instance=religion)

    if request.method == "POST":
        form = ReligionForm(request.POST, instance=religion)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search_religion')
            except Exception as e:
                pass

    return render(request, 'Religion_caste/update_religion.html', {'form': form})


def delete_religion(request, id):
    religion = get_object_or_404(Religion_master, id=id)
    try:
        religion.delete()
    except Exception as e:
        pass
    return redirect('/search_religion')


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
            return redirect('/search_maincaste')
    else:
        form = MainCasteForm()
    return render(request, 'Religion_caste/maincaste_create.html', {'form': form})


def search_maincaste(request):
    maincastes = MainCaste_master.objects.all()
    return render(request, "Religion_caste/search_maincaste.html", {'maincastes': maincastes})


def update_maincaste(request, id):
    maincaste = get_object_or_404(MainCaste_master, id=id)
    form = MainCasteForm(instance=maincaste)

    if request.method == "POST":
        form = MainCasteForm(request.POST, instance=maincaste)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search_maincaste')
            except Exception as e:
                pass

    return render(request, 'Religion_caste/update_maincaste.html', {'form': form})


def delete_maincaste(request, id):
    maincaste = get_object_or_404(MainCaste_master, id=id)
    try:
        maincaste.delete()
    except Exception as e:
        pass
    return redirect('/search_maincaste')


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
            return redirect('/search_subcaste')
    else:
        form = SubCasteForm()
    return render(request, 'Religion_caste/subcaste_create.html', {'form': form})


def search_subcaste(request):
    subcastes = SubCaste_master.objects.all()
    return render(request, "Religion_caste/search_subcaste.html", {'subcastes': subcastes})


def update_subcaste(request, id):
    subcaste = get_object_or_404(SubCaste_master, id=id)
    form = SubCasteForm(instance=subcaste)

    if request.method == "POST":
        form = SubCasteForm(request.POST, instance=subcaste)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search_subcaste')
            except Exception as e:
                pass
    return render(request, 'Religion_caste/update_subcaste.html', {'form': form})


def delete_subcaste(request, id):
    subcaste = get_object_or_404(SubCaste_master, id=id)
    try:
        subcaste.delete()
    except Exception as e:
        pass
    return redirect('/search_subcaste')


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
            return redirect('/search_state')
    else:
        form = StateForm()
    return render(request, 'state_city/state_create.html', {'form': form})


def search_state(request):
    sal = State_master.objects.all()
    return render(request, "state_city/search_state.html", {'subm': sal})


def update_state(request, id):
    state = get_object_or_404(State_master, id=id)
    form = StateForm(instance=state)

    if request.method == "POST":
        form = StateForm(request.POST, instance=state)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search_state')
            except Exception as e:
                pass
    return render(request, 'state_city/update_state.html', {'form': form})


def delete_state(request, id):
    state = State_master.objects.get(id=id)
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
    states = State_master.objects.all()
    cities = CityForm(request.POST or None)
    if cities.is_valid():
        cities.save()
        return redirect('/search_city')
    else:
        context['form'] = cities

    context["states"] = states
    return render(request, "state_city/city_create.html", context)


def search_city(request):
    sal = City_master.objects.all()
    return render(request, "state_city/search_city.html", {'subm': sal})


def update_city(request, id):
    branch = City_master.objects.get(id=id)
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


def delete_city(request, id):
    city = City_master.objects.get(id=id)
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

""" Tehsil views """


def create_tehsil(request):
    context = {}
    states = State_master.objects.all()
    tehsil = TehsilMasterForm(request.POST or None)
    if tehsil.is_valid():
        tehsil.save()
        return redirect('/search_tehsil')
    else:
        context['form'] = tehsil
    context["states"] = states
    return render(request, "state_city/tehsil_create.html", context)


def search_tehsil(request):
    tehsils = Tehsil_master.objects.all()
    return render(request, "state_city/search_tehsil.html", {'tehsils': tehsils})


def update_tehsil(request, id):
    tehsil = get_object_or_404(Tehsil_master, id=id)
    form = TehsilMasterForm(instance=tehsil)

    if request.method == "POST":
        form = TehsilMasterForm(request.POST, instance=tehsil)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search_tehsil')
            except Exception as e:
                pass

    return render(request, 'state_city/update_tehsil.html', {'form': form})


def delete_tehsil(request, id):
    tehsil = get_object_or_404(Tehsil_master, id=id)
    try:
        tehsil.delete()
    except Exception as e:
        pass
    return redirect('/search_tehsil')


"""# ****************************************************************************************************************************************************
# ****************************************************************************************************************************************************  """

""" Nationality views """


def nationality_create(request):
    if request.method == 'POST':
        form = NationalityMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/search_nationality')
    else:
        form = NationalityMasterForm()
    return render(request, 'Religion_caste/nationality_create.html', {'form': form})


def search_nationality(request):
    nationalities = Nationality_master.objects.all()
    return render(request, "Religion_caste/search_nationality.html", {'nationalities': nationalities})


def update_nationality(request, id):
    nationality = get_object_or_404(Nationality_master, id=id)
    form = NationalityMasterForm(instance=nationality)

    if request.method == "POST":
        form = NationalityMasterForm(request.POST, instance=nationality)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search_nationality')
            except Exception as e:
                pass

    return render(request, 'Religion_caste/update_nationality.html', {'form': form})


def delete_nationality(request, id):
    nationality = get_object_or_404(Nationality_master, id=id)
    try:
        nationality.delete()
    except Exception as e:
        pass
    return redirect('/search_nationality')


"""# ****************************************************************************************************************************************************
# ****************************************************************************************************************************************************  """

""" Mother Tongue views """


def mothertongue_create(request):
    if request.method == 'POST':
        form = MotherTongueMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('added successfully')
    else:
        form = MotherTongueMasterForm()
    return render(request, 'Details/mothertongue_create.html', {'form': form})


def search_mothertongue(request):
    mothertongues = motherTongue_master.objects.all()
    return render(request, "Details/search_mothertongue.html", {'mothertongues': mothertongues})


def update_mothertongue(request, id):
    mothertongue = get_object_or_404(motherTongue_master, id=id)
    form = MotherTongueMasterForm(instance=mothertongue)

    if request.method == "POST":
        form = MotherTongueMasterForm(request.POST, instance=mothertongue)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search_mothertongue')
            except Exception as e:
                pass

    return render(request, 'Details/update_mothertongue.html', {'form': form})


def delete_mothertongue(request, id):
    mothertongue = get_object_or_404(motherTongue_master, id=id)
    try:
        mothertongue.delete()
    except Exception as e:
        pass
    return redirect('/search_mothertongue')


"""# ****************************************************************************************************************************************************
# ****************************************************************************************************************************************************  """

""" School Board views """


def schoolboard_create(request):
    if request.method == 'POST':
        form = SchoolBoardMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/search_schoolboard')
    else:
        form = SchoolBoardMasterForm()
    return render(request, 'Details/schoolboard_create.html', {'form': form})


def search_schoolboard(request):
    schoolboards = SchoolBoard_master.objects.all()
    return render(request, "Details/search_schoolboard.html", {'schoolboards': schoolboards})


def update_schoolboard(request, id):
    schoolboard = get_object_or_404(SchoolBoard_master, id=id)
    form = SchoolBoardMasterForm(instance=schoolboard)

    if request.method == "POST":
        form = SchoolBoardMasterForm(request.POST, instance=schoolboard)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search_schoolboard')
            except Exception as e:
                pass

    return render(request, 'Details/update_schoolboard.html', {'form': form})


def delete_schoolboard(request, id):
    schoolboard = get_object_or_404(SchoolBoard_master, id=id)
    try:
        schoolboard.delete()
    except Exception as e:
        pass
    return redirect('/search_schoolboard')


"""# ****************************************************************************************************************************************************
# ****************************************************************************************************************************************************  """

""" student views """


def student_create(request):
    context = {}
    stdclass = StdClass_master.objects.all()
    sections = Section_master.objects.all()
    castem = MainCaste_master.objects.all()
    castes = SubCaste_master.objects.all()
    religions = Religion_master.objects.all()
    nations = Nationality_master.objects.all()
    mothertongues = motherTongue_master.objects.all()
    cities = City_master.objects.all()
    tehsils = Tehsil_master.objects.all()
    states = State_master.objects.all()

    if request.method == 'POST':
        form = StudentPersonalDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/search_student')
        else:
            messages.error(request, form.errors)
    else:
        form = StudentPersonalDetailsForm()

    context['form'] = form
    context['stdclass'] = stdclass
    context['sections'] = sections
    context['castem'] = castem
    context['castes'] = castes
    context['religions'] = religions
    context['nations'] = nations
    context['mothertongues'] = mothertongues
    context['cities'] = cities
    context['tehsils'] = tehsils
    context['states'] = states

    return render(request, 'Details/student_create.html', context)


def search_student(request):
    students = StudentPersonalDetails.objects.all()
    return render(request, "Details/student_search.html", {'students': students})


def update_student(request, id):
    student = get_object_or_404(StudentPersonalDetails, id=id)
    form = StudentPersonalDetailsForm(instance=student)

    if request.method == "POST":
        form = StudentPersonalDetailsForm(request.POST, instance=student)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search_student')
            except Exception as e:
                pass

    return render(request, 'Details/update_student.html', {'form': form})


def delete_student(request, id):
    student = get_object_or_404(StudentPersonalDetails, id=id)
    try:
        student.delete()
    except Exception as e:
        pass
    return redirect('/search_student')


"""# ****************************************************************************************************************************************************
# **************************************************************************************************************************************************** """

"""previous_school views """


def previous_school_create(request):
    context = {}
    stdname = StudentPersonalDetails.objects.all()
    boards = SchoolBoard_master.objects.all()
    cities = City_master.objects.all()
    tehsils = Tehsil_master.objects.all()
    states = State_master.objects.all()
    form = PreviousSchoolDetailsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse('added successfully')
    else:
        context['form'] = form

    context["stdname"] = stdname
    context["boards"] = boards
    context['cities'] = cities
    context['tehsils'] = tehsils
    context['states'] = states
    return render(request, "Details/previous_school_create.html", context)


def search_previousschool(request):
    previousschools = PreviousSchoolDetails.objects.all()
    return render(request, "Details/search_previousschool.html", {'previousschools': previousschools})


def update_previousschool(request, id):
    previousschool = get_object_or_404(PreviousSchoolDetails, id=id)
    form = PreviousSchoolDetailsForm(instance=previousschool)

    if request.method == "POST":
        form = PreviousSchoolDetailsForm(request.POST, instance=previousschool)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search_previousschool')
            except Exception as e:
                pass

    return render(request, 'Details/update_previousschool.html', {'form': form})


def delete_previousschool(request, id):
    previousschool = get_object_or_404(PreviousSchoolDetails, id=id)
    try:
        previousschool.delete()
    except Exception as e:
        pass
    return redirect('/search_previousschool')


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
