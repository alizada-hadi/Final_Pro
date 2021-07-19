from .models import CurriculumUploadList
from csfmis.settings import DEBUG
from django.contrib import admin
from .models import Department, Curriculum


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("dep_name", "dep_status", "dep_publish_date",)


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = (
        "department",
        "curr_code",
        "slug",
        "curr",
        "curr_name",
    )
    prepopulated_fields = {'slug': ('curr_name',)}


admin.site.register(CurriculumUploadList)
