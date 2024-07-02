from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import *
from .models import *
from django.contrib import messages
from django.db.models import F
from io import BytesIO
from random import sample

"""Views for Employee Table"""


@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
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


""" Created Exam views by Kunal Durudkar"""


def add_subject(request):
    if request.method == 'POST':
        form = subjectmasterform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(add_question)
    else:
        form = subjectmasterform()
    return render(request, 'ExamPaper/add_subject.html', {'form': form})


def search_subject(request):
    sal = subjectmaster.objects.all()
    return render(request, "ExamPaper/searchsubject.html", {'subm': sal})


def update_subject(request, id):
    branch = subjectmaster.objects.get(id=id)
    form = subjectmasterform(initial={'subjectname': branch.subjectname, 'description': branch.description, })
    if request.method == "POST":
        form = subjectmasterform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/search_subject')
            except Exception as e:
                pass
    return render(request, 'ExamPaper/updatesubject.html', {'form': form})


def delete_subject(request, id):
    subject = subjectmaster.objects.get(id=id)
    try:
        subject.delete()
    except:
        pass
    return redirect('/search_subject')


# *******************************************************************************************************************#
# *******************************************************************************************************************#
def add_question(request):
    context = {}
    sub = subjectmaster.objects.all()

    if request.method == 'POST':
        print(request.POST.get('question_type'))
        print(request.POST)
        questionid = request.POST.get('question_type')
        subforms = ""
        print(questionid)
        if questionid == "Subjective":
            subforms = subjectivequeform(request.POST, request.FILES)
            print("hello subject")
        elif questionid == "MCQ":
            print("hello mcq")
            subforms = mcqqueform(request.POST or None)
        print(subforms)
        print(subforms.is_valid())
        # x = request.POST
        # print(type(x))

        if subforms.is_valid():
            subforms.save()
            return HttpResponse('Question added successfully')
        else:
            # print(request.POST)
            messages.error(request, subforms.errors)
            context['form'] = mcqqueform
            return HttpResponse('Question error ')
    else:
        context["sub"] = sub
        return render(request, 'ExamPaper/add_question.html', context)


def search_question_bank(request):
    sal = questionbank.objects.all()
    return render(request, "ExamPaper/searchquestionbank.html", {'quesbm': sal})


def update_question_bank(request, id):
    question = questionbank.objects.get(id=id)

    if question.question_type == 'MCQ':
        form = mcqqueform(initial={'question_type': question.question_type, 'subject': question.subject,
                                   'question': question.question, 'image': question.image, 'option1': question.option1,
                                   'option2': question.option2, 'option3': question.option3,
                                   'option4': question.option4, 'option_choices': question.option_choices, })
    elif question.question_type == 'Subjective':
        form = subjectivequeform(initial={'question_type': question.question_type, 'subject': question.subject,
                                          'question': question.question, 'image': question.image,
                                          'solution': question.solution,
                                          'question_weightage': question.question_weightage, })

    if request.method == 'POST':
        form = mcqqueform(request.POST, instance=question)  # Use mcqqueform as a default
        if question.question_type == 'Subjective':
            form = subjectivequeform(request.POST, instance=question)

        if form.is_valid():
            try:
                form.save()
                model = form.instance
                # Redirect to a success page or the updated question page
                return redirect('/search_question_bank')
            except Exception as e:
                pass

    return render(request, 'ExamPaper/updatequestionbank.html', {'form': form, 'question': question})


def delete_question_bank(request, id):
    employee = questionbank.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/search_question_bank')


# ****************************************************************************************************************************#
# ****************************************************************************************************************************#
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def download_questions(request):
    context = {}
    if request.method == 'POST':
        question_type = request.POST.get('question_type')
        subject = request.POST.get('subject')
        num_questions = int(request.POST.get('num_questions', 10))  # Default to 10 questions
        print(request.POST.get('subject'))
        print(request.POST)

        # database to retrieve questions
        questions = questionbank.objects.filter(question_type=question_type, subject=subject)
        if questions.count() < num_questions:
            num_questions = questions.count()
        # Randomly select questions
        selected_questions = sample(list(questions), num_questions)
        context = {
            'questions': selected_questions,
        }
        # Generate and return a PDF response
        pdf = render_to_pdf('ExamPaper/questions_template.html', context)
        if pdf:
            return HttpResponse(pdf, content_type='application/pdf')
    # If the request method is not POST or other cases, return an empty form
    subject_list = subjectmaster.objects.all()
    context["subject_list"] = subject_list
    return render(request, 'ExamPaper/download_questions.html', context)
