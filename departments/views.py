from django.shortcuts import render
from django.urls import reverse_lazy
from departments.models import Curriculum, Department
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    DeleteView
)
from .forms import DepForm, CurriculumForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    form_class = DepForm
    template_name = "departments/department_form.html"
    success_url = reverse_lazy("department-list")


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = "departments/department/department_list.html"
    context_object_name = "departments"


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    fields = '__all__'
    success_url = reverse_lazy("department-list")


@login_required
def department_detail(request, pk):
    department = Department.objects.get(pk=pk)
    curriculums = [[], [], [], [], [], [], [], []]
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
        "curriculums": curriculums
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
