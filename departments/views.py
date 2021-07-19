from .models import CurriculumUploadList
import csv
from django.http.response import HttpResponse
from students.models import Student
from staff.models import Staff
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from departments.models import Curriculum, Department
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    DeleteView
)
from .forms import DepForm, CurriculumForm, CurriculumUploadForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .decorators import group_required
from django.utils.decorators import method_decorator


@group_required("admin")
def department_create_view(request):
    if request.method == "POST":
        form = DepForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DepForm()
    context = {
        "form": form
    }
    return render(request, "departments/department_form.html", context)


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = "departments/department/department_list.html"
    context_object_name = "departments"


@group_required("admin", "dep_doan")
def department_update_view(request, pk):
    obj = get_object_or_404(Department, pk=pk)
    form = DepForm()
    if request.method == "POST":
        form = DepForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("department-list")
    else:
        form = DepForm(instance=obj)
    context = {
        "form": form
    }
    return render(request, "departments/department/update.html", context)


@login_required
@group_required("admin", "dep_doan", "Instructor")
def department_detail(request, pk):
    department = Department.objects.get(pk=pk)
    members = []
    students = []
    curriculums = [[], [], [], [], [], [], [], []]
    for staff in Staff.objects.all():
        if staff.department.id == pk:
            members.append(staff)
    for student in Student.objects.all():
        if student.department.id == pk:
            students.append(student)

    for c in Curriculum.objects.all():
        if c.department.id == pk and c.curr_semester == "First":
            curriculums[0].append(c)
        elif c.department.id == pk and c.curr_semester == "Second":
            curriculums[1].append(c)
        elif c.department.id == pk and c.curr_semester == "Thrid":
            curriculums[3].append(c)
        elif c.department.id == pk and c.curr_semester == "Fourth":
            curriculums[4].append(c)
        elif c.department.id == pk and c.curr_semester == "Fifth":
            curriculums[5].append(c)
        elif c.department.id == pk and c.curr_semester == "Sixth":
            curriculums[6].append(c)
        elif c.department.id == pk and c.curr_semester == "Seventh":
            curriculums[7].append(c)
        elif c.department.id == pk and c.curr_semester == "Eighth":
            curriculums[8].append(c)
    context = {
        "department": department,
        "curriculums": curriculums,
        "members": members,
        "students": students
    }
    return render(request, "departments/department/department_detail.html", context)

# curriculums views


class CurriculumCreateView(LoginRequiredMixin, CreateView):
    model = Curriculum
    form_class = CurriculumForm
    template_name = "departments/curriculum_form.html"


class CurriculumDetailView(LoginRequiredMixin, DetailView):
    model = Curriculum
    template_name = "departments/curriculum/curriculum_detail.html"


@login_required
def curriculum_list(request):
    information_system = [[], [], [], [], [], [], [], []]
    software_engineering = [[], [], [], [], [], [], [], []]
    information_technology = [[], [], [], [], [], [], [], []]
    for i in Curriculum.objects.all():
        if i.department.dep_name == "Information System" and i.curr_semester == "First":
            information_system[0].append(i)
        elif i.department.dep_name == "Information System" and i.curr_semester == "Second":
            information_system[1].append(i)
        elif i.department.dep_name == "Information System" and i.curr_semester == "Third":
            information_system[2].append(i)
        elif i.department.dep_name == "Information System" and i.curr_semester == "Fourth":
            information_system[3].append(i)
        elif i.department.dep_name == "Information System" and i.curr_semester == "Fifth":
            information_system[4].append(i)
        elif i.department.dep_name == "Information System" and i.curr_semester == "Sixth":
            information_system[5].append(i)
        elif i.department.dep_name == "Information System" and i.curr_semester == "Seventh":
            information_system[6].append(i)
        elif i.department.dep_name == "Information System" and i.curr_semester == "Eighth":
            information_system[7].append(i)

    for s in Curriculum.objects.all():
        if s.department.dep_name == "Software Engineering" and s.curr_semester == "First":
            software_engineering[0].append(s)
        elif s.department.dep_name == "Software Engineering" and s.curr_semester == "Second":
            software_engineering[1].append(s)
        elif s.department.dep_name == "Software Engineering" and s.curr_semester == "Third":
            software_engineering[2].append(s)
        elif s.department.dep_name == "Software Engineering" and s.curr_semester == "Fourth":
            software_engineering[3].append(s)
        elif s.department.dep_name == "Software Engineering" and s.curr_semester == "Fifth":
            software_engineering[4].append(s)
        elif s.department.dep_name == "Software Engineering" and s.curr_semester == "Sixth":
            software_engineering[5].append(s)
        elif s.department.dep_name == "Software Engineering" and s.curr_semester == "Seventh":
            software_engineering[6].append(s)
        elif s.department.dep_name == "Software Engineering" and s.curr_semester == "Eighth":
            software_engineering[7].append(s)

    for t in Curriculum.objects.all():
        if t.department.dep_name == "Information Technology" and t.curr_semester == "First":
            information_technology[0].append(t)
        elif t.department.dep_name == "Information Technology" and t.curr_semester == "Second":
            information_technology[1].append(t)
        elif t.department.dep_name == "Information Technology" and t.curr_semester == "Third":
            information_technology[2].append(t)
        elif t.department.dep_name == "Information Technology" and t.curr_semester == "Fourth":
            information_technology[3].append(t)
        elif t.department.dep_name == "Information Technology" and t.curr_semester == "Fifth":
            information_technology[4].append(t)
        elif t.department.dep_name == "Information Technology" and t.curr_semester == "Sixth":
            information_technology[5].append(t)
        elif t.department.dep_name == "Information Technology" and t.curr_semester == "Seventh":
            information_technology[6].append(t)
        elif t.department.dep_name == "Information Technology" and t.curr_semester == "Eighth":
            information_technology[7].append(t)

    context = {
        "info_sys": information_system,
        "soft_eng": software_engineering,
        "info_tech": information_technology
    }
    return render(request, "departments/curriculum/curriculum_list.html", context)


class CurriculumUpdateView(LoginRequiredMixin, UpdateView):
    model = Curriculum
    fields = '__all__'
    success_url = reverse_lazy("curriculum-list")


class CurriculumDeleteView(LoginRequiredMixin, DeleteView):
    model = Curriculum
    template_name = "departments/curriculum_confirm_delete.html"


class CurriculumUploadView(CreateView):
    model = CurriculumUploadList
    template_name = "departments/curriculum/upload.html"
    fields = ["csv_file"]
    success_url = reverse_lazy("curriculum-upload")


def download_csv_file(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="curriculum_template.csv"'

    writer = csv.writer(response)
    writer.writerow([
        "department",
        "curr_code",
        "curr",
        "curr_name",
        "curr_credit",
        "curr_semester",
        "curr_type",
        "curr_description"
    ])

    return response
