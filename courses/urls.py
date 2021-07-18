from django.urls import path
from . import views


urlpatterns = [
    path("courses/mine/", views.ManageCourseListView.as_view(), name="course-list"),
    path("course/create/", views.CourseCreateView.as_view(), name="course-create"),
    path("<int:pk>/course/", views.CourseUpdateView.as_view(), name="course-update"),
    path("<int:pk>/course/delete/",
         views.CourseDeleteView.as_view(), name="course-delete"),
    path("course/<int:pk>/modules/",
         views.CourseModuleUpdateView.as_view(), name="course-moudle-update"),
    path("module/<int:module_id>/content/<model_name>/create/",
         views.CourseContentCreateUpdateView.as_view(), name="module-content-create"),
    path("module/<int:module_id>/content/<model_name>/<id>/",
         views.CourseContentCreateUpdateView.as_view(), name="module-content-update"),
    path("content/<int:id>/delete/",
         views.ContentDeleteView.as_view(), name="content-delete"),
    path("module/<int:module_id>/", views.ModuleContentListView.as_view(),
         name="module_content_list"),


    #
    path("courses/", views.CourseListView.as_view(), name="all-courses"),
    path("curriculum/<slug:curriculum>/",
         views.CourseListView.as_view(), name="course-list-curriculum"),
    path("<slug:slug>/", views.CourseDetailView.as_view(), name="course_detail"),
    path("course/join/<slug:slug>/", views.join_course_view, name="join-to-course"),
    path("course/assignment/module/<int:pk>/",
         views.AssignmentCreateView.as_view(), name="assignment-create"),
    path("assignment/<slug:slug>/detail/",
         views.AssignmentDetailView.as_view(), name="assignment-detail"),
]
