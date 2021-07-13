from os import name
from django.urls import path
from . import views

urlpatterns = [
    path("calendar/", views.CalendarViewNew.as_view(), name="calendar"),
    path("event/new/",  views.EventCreateView.as_view(), name="new-event"),
    path("assignment/create/", views.AssignmentCreateView.as_view(),
         name="assignment-create"),
    path("assignments/", views.AssignmentListView.as_view(), name="assignment-list"),
    path("staff/assignments/", views.AssignmentStaffListView.as_view(),
         name="staff-assignment"),
    path("assignment/<slug:slug>/",
         views.AssignmentUpdateView.as_view(), name="assignment-update"),
    path("assignment/<slug:slug>/detail/",
         views.AssignmentDetailView.as_view(),  name="assignment-detail"),
    path("respond/<slug:slug>/",
         views.check_assignment_view, name="responds"),
    path("respond/detail/<int:pk>/", views.respond_detail, name="respond-detail")
]
