from django.contrib import admin

# Register your models here.
from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "course",
        "total_score",
    )
