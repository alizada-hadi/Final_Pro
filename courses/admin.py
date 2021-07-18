from django.contrib import admin
from django.db import models
from .models import Course, Module, Session, Assignment


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        "session",
        "session_type",
    )


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "assign_date",
        "due_date",
    )
    prepopulated_fields = {
        "slug": ("title",)
    }


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "curriculum",
        "code",
        "title",
        'slug',
        "created_at",
    )
    list_filter = (
        "title",
        "slug",
    )
    search_fields = (
        "slug",
        "title",
        "code",
    )
    prepopulated_fields = {
        "slug": ("title",)
    }
    inlines = [ModuleInline]
