from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from students.models import Student
from staff.models import Staff


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_student == True:
                login(request, user)
                return redirect("student-profile")
            elif user.is_staff == True:
                login(request, user)
                return redirect("staff-profile")
    return render(request, "Authentication/main.html")
