from django.urls import path
from . import views

urlpatterns = [
    path("create/department/", views.department_create_view,
         name="department-create"),
    path('departments/', views.DepartmentListView.as_view(), name="department-list"),
    path("department/<int:pk>/", views.department_update_view,
         name="department-update"),
    path("department/<int:pk>/detail/",
         views.department_detail, name="department-detail"),
    #     curriclum urls
    path("curriculum/create/", views.CurriculumCreateView.as_view(),
         name="curriculum-create"),
    path("curriculum/<int:pk>/detail/",
         views.CurriculumDetailView.as_view(), name="curriculum-detail"),
    path("curriculums/", views.curriculum_list, name="curriculum-list"),
    path("curriculum/<int:pk>/update/",
         views.CurriculumUpdateView.as_view(), name="curriculum-update"),
    path("curriculum/<int:pk>/delete/",
         views.CurriculumDeleteView.as_view(), name="curriculum-delete"),
    path("curriculum/upload/list/",
         views.CurriculumUploadView.as_view(), name="curriculum-upload"),
    path("downloadcsv/", views.download_csv_file, name="download-csv"),
]
