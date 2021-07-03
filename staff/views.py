from django.shortcuts import render, redirect
from .forms import StaffSignUpForm, StaffProfileDetailInfo, StaffUserUpdateForm
from .models import Staff
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User
from django.views.generic import (
    CreateView,
    ListView
)
from .decorators import staff_required


class StaffSignupView(LoginRequiredMixin, CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = "staff/staff_register.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'staff'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('/')


class StaffListView(LoginRequiredMixin, ListView):
    model = Staff
    template_name = "staff/staff_list.html"
    context_object_name = "staffs"


@login_required
@staff_required
def staffProfile(request):
    return render(request, "staff/profile.html")


@login_required
@staff_required
def staff_profile_detail_info(request):
    if request.method == "POST":
        u_form = StaffUserUpdateForm(request.POST, instance=request.user)
        form = StaffProfileDetailInfo(
            request.POST, request.FILES, instance=request.user.staff)
        if form.is_valid() and u_form.is_valid():
            form.save()
            u_form.save()
            return redirect("staff-profile")
    else:
        form = StaffProfileDetailInfo(instance=request.user.staff)
        u_form = StaffUserUpdateForm(instance=request.user)
    context = {
        "form": form,
        "u_form": u_form
    }
    return render(request, "staff/staff_profile_detail_info.html", context)
