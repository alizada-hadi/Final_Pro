from django.contrib import admin
from .models import Staff, StaffEducation,  StaffJobExp


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        "staff_id",
        "first_name",
        "last_name",
        "dob",
        "department",
    )
