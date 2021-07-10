import datetime
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    ListView,
    DetailView
)
from .forms import StudentSignUpForm, UserUpdateForm, UserProfileUpdateForm
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from .decorators import student_required
from django.contrib.auth.decorators import login_required
from .models import Category, Student
from courses.models import Course
from staff.decorators import staff_required
from departments.models import Curriculum
from results.models import Result


class StudentSignUpView(LoginRequiredMixin, CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = "students/student_register.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form, **kwargs):
        user = form.save()
        return redirect('/')


@login_required
@student_required
def student_profile(request):
    categories = Category.objects.all()
    courses = Course.objects.filter(students=request.user.student)
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = UserProfileUpdateForm(
        request.POST, request.FILES, instance=request.user.student)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'categories': categories,
        "courses": courses
    }
    return render(request, "students/profile.html", context)


@login_required
@student_required
def student_profile_completion(request):
    category = Category.objects.all()
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.student)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("student-profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.student)
    context = {
        "u_form": u_form,
        "p_form": p_form,
        "categories": category
    }
    return render(request, "students/profile_complete.html", context)


@login_required
def logoutPage(request):
    logout(request)
    return redirect("login")


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'students'
    template_name = "students/student_list.html"


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = "students/course/list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user.student])

    def get_context_data(self, *args, **kwargs):
        context = super(StudentCourseListView,
                        self).get_context_data(*args, **kwargs)
        context["items"] = Course.objects.filter(
            visited_at=datetime.date.today())
        context["subjects"] = Curriculum.objects.filter(
            curr_semester=self.request.user.student.semester)
        context["classmates"] = Student.objects.filter(
            semester=self.request.user.student.semester, department=self.request.user.student.department)

        return context


class StudentCourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "students/course/detail.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user.student])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = datetime.date.today()
        course = self.get_object()
        if "module_id" in self.kwargs:
            context['module'] = course.modules.get(
                id=self.kwargs['module_id']
            )
        else:
            context['module'] = course.modules.all()[0]
        return context


@login_required
@staff_required
def student_detail_view(request, pk):
    student = Student.objects.get(pk=pk)
    semesters = [[], [], [], [], [], [], [], []]
    for r in student.result_set.all():
        if r.course.curriculum.curr_semester == "First":
            semesters[0].append(r)
        elif r.course.curriculu.curr_semester == "Second":
            semesters[1].append(r)
        elif r.course.curriculu.curr_semester == "Thrid":
            semesters[1].append(r)
        elif r.course.curriculu.curr_semester == "Fourth":
            semesters[1].append(r)
        elif r.course.curriculu.curr_semester == "Fifth":
            semesters[1].append(r)
        elif r.course.curriculu.curr_semester == "Sixth":
            semesters[1].append(r)
        elif r.course.curriculu.curr_semester == "Seventh":
            semesters[1].append(r)
        elif r.course.curriculu.curr_semester == "Eighth":
            semesters[1].append(r)

    context = {
        'student': student,
        "semesters": semesters
    }
    return render(request, "students/student_detail.html", context)


@login_required
@student_required
def semester_report(request):
    test_total = 0
    project_total = 0
    home_total = 0
    class_total = 0
    final_total = 0
    total_credit = 0
    percentage = 0
    total_curriculum = 0
    status = ""
    results = Result.objects.filter(student=request.user.student)
    for c in Curriculum.objects.all():
        if c.curr_semester == request.user.student.semester and c.department == request.user.student.department:
            total_curriculum += c.curr_credit
    for r in results:
        test_total += r.mid_term_exam
        project_total += r.project_score
        home_total += r.home_work_score
        class_total += r.class_activity_score
        final_total += r.final_exam
        total_credit += r.course.curriculum.curr_credit
        percentage += r.total() / len(results)

    context = {
        "results": results,
        "test_total": test_total,
        "project_total": project_total,
        "home_total": home_total,
        "class_total": class_total,
        "final_total": final_total,
        "total_credit": total_credit,
        "total": test_total + project_total + home_total + class_total + final_total,
        "percentage": percentage,
        "total_curriculum": total_curriculum

    }
    return render(request, "students/semester_report.html", context)


@login_required
@student_required
def general_report(request):
    semesters = [[], [], [], [], [], [], [], []]
    first_semester_total = 0
    passed_credit = 0
    percentage = 0
    results = request.user.student.result_set.count()
    for result in request.user.student.result_set.all():
        first_semester_total += result.total()
        passed_credit += result.course.curriculum.curr_credit
        percentage += result.total() / results
    for r in request.user.student.result_set.all():
        if r.course.curriculum.curr_semester == "First":
            semesters[0].append(r)
        elif r.course.curriculum.curr_semester == "Second":
            semesters[1].append(r)
        elif r.course.curriculum.curr_semester == "Thrid":
            semesters[1].append(r)
        elif r.course.curriculum.curr_semester == "Fourth":
            semesters[1].append(r)
        elif r.course.curriculum.curr_semester == "Fifth":
            semesters[1].append(r)
        elif r.course.curriculum.curr_semester == "Sixth":
            semesters[1].append(r)
        elif r.course.curriculum.curr_semester == "Seventh":
            semesters[1].append(r)
        elif r.course.curriculum.curr_semester == "Eighth":
            semesters[1].append(r)
    context = {
        "semesters": semesters,
        "first_semester_total": first_semester_total,
        "passed_credit": passed_credit,
        "percentage": percentage
    }
    return render(request, "students/general_report.html", context)
