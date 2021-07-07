from django.urls import path
from . import views


urlpatterns = [
    path("course/<int:pk>/create/result/",
         views.create_result, name="create-result"),
    path("course/update/result/<int:pk>",
         views.edit_result, name="update-result"),
    path("course/all_result/<int:pk>/", views.all_result_view, name="all-results")
]
