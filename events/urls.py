from os import name
from django.urls import path
from . import views

urlpatterns = [
    path("calendar/", views.CalendarViewNew.as_view(), name="calendar"),
    path("event/new/",  views.EventCreateView.as_view(), name="new-event"),
    path("respond/<slug:slug>/",
         views.check_assignment_view, name="responds"),
    path("respond/detail/<int:pk>/", views.respond_detail, name="respond-detail"),
    path("student/calenar/view/", views.StudentCalenderListView.as_view(),
         name="student-calendar"),
]
