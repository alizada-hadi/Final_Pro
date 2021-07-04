from csfmis.settings import DEBUG
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("", include("departments.urls")),
    path("", include("students.urls")),
    path("", include("staff.urls")),
    path("", include("accounts.urls")),
    path("", include("courses.urls")),
    path('ckeditor/', include("ckeditor_uploader.urls")),
]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
