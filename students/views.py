from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView
)
from .forms import StudentSignUpForm, UserUpdateForm, UserProfileUpdateForm
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from .decorators import student_required
from django.contrib.auth.decorators import login_required
from .models import Category


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


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_student == True:
                login(request, user)
                return redirect("student-profile")
    return render(request, "Authentication/main.html")


@login_required
@student_required
def student_profile(request):
    return render(request, "students/profile.html")


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
