from django.urls import path
from . import views

urlpatterns = [
    path("staff/register/", views.StaffSignupView.as_view(), name="staff-register"),
    path("stffs/", views.StaffListView.as_view(), name="staff-list"),
    path("staff/profile/", views.staffProfile, name="staff-profile"),
    path("staff/profile/detail/", views.staff_profile_detail_info,
         name="staff-profile-detail"),
]
