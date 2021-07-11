from django.urls import path
from . import views

urlpatterns = [
    path("calendar/", views.CalendarViewNew.as_view(), name="calendar")
]
