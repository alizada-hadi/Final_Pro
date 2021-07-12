from django.urls import path
from . import views

urlpatterns = [
    path("calendar/", views.CalendarViewNew.as_view(), name="calendar"),
    path("event/new/",  views.EventCreateView.as_view(), name="new-event"),
    path("assignment/create/", views.AssignmentCreateView.as_view(),
         name="assignment-create"),
    path("assignments/", views.AssignmentListView.as_view(), name="assignment-list"),
    path("assignment/<slug:slug>/",
         views.AssignmentUpdateView.as_view(), name="assignment-update"),
    path("assignment/<slug:slug>/detail/",
         views.AssignmentDetailView.as_view(),  name="assignment-detail"),
]
