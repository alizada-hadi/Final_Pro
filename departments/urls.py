from django.urls import path
from . import views

urlpatterns = [
    path("create/department/", views.DepartmentCreateView.as_view(),
         name="department-create"),
    path('departments/', views.DepartmentListView.as_view(), name="department-list"),
    path("department/<int:pk>/", views.DepartmentUpdateView.as_view(),
         name="department-update"),
    path("department/<int:pk>/detail/",
         views.department_detail, name="department-detail"),
    #     curriclum urls
    path("curriculum/create/", views.CurriculumCreateView.as_view(),
         name="curriculum-create"),
    path("curriculum/<slug:slug>/detail/",
         views.CurriculumDetailView.as_view(), name="curriculum-detail"),
    path("curriculums/", views.curriculum_list, name="curriculum-list"),
    path("curriculum/<slug:slug>/update/",
         views.CurriculumUpdateView.as_view(), name="curriculum-update"),
    path("curriculum/<slug:slug>/delete/",
         views.CurriculumDeleteView.as_view(), name="curriculum-delete"),
]
