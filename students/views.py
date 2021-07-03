from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    ListView
)
from .forms import StudentSignUpForm, UserUpdateForm, UserProfileUpdateForm
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from .decorators import student_required
from django.contrib.auth.decorators import login_required
from .models import Category, Student


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
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = UserProfileUpdateForm(
        request.POST, request.FILES, instance=request.user.student)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'categories': categories
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
