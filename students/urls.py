from django.urls import path
from . import views


urlpatterns = [
    path("students/register/",  views.StudentSignUpView.as_view(),
         name="student-register"),
    path("student/profile/", views.student_profile, name="student-profile"),
    path("student/profile/complete/", views.student_profile_completion,
         name="student-profile-complete"),
    path("student/logout/", views.logoutPage, name="logout"),
    path("students/", views.StudentListView.as_view(), name="student-list"),
    #     student's course

    path("students/courses/",  views.StudentCourseListView.as_view(),
         name="student-course-list"),
    path("students/course/<int:pk>/",
         views.StudentCourseDetailView.as_view(), name="student-course-detail"),
    path("student/course/<pk>/<module_id>/",
         views.StudentCourseDetailView.as_view(), name="student-course-detail-module"),
    path("students/detail/<int:pk>/",
         views.student_detail_view, name="student-detail")
]
