from django.urls import path
from . import views


urlpatterns = [
    path("course/<int:pk>/create/result/",
         views.create_result, name="create-result"),
    path("course/update/result/", views.edit_result, name="update-result"),
]
