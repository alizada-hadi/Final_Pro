from django.urls import path
from . import views


urlpatterns = [
    path("students/register/",  views.StudentSignUpView.as_view(),
         name="student-register"),
    path("login/", views.login_view, name="login"),
    path("student/profile/", views.student_profile, name="student-profile"),
    path("student/profile/complete/", views.student_profile_completion,
         name="student-profile-complete"),
]
