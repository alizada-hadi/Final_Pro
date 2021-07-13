from django.contrib import admin
from . import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    list_display = [
        'id', 'title', 'user', 'is_active', 'is_deleted', 'created_at',
        'updated_at'
    ]
    list_filter = ['is_active', 'is_deleted']
    search_fields = ['title']


@admin.register(models.EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    model = models.EventMember
    list_display = ['id', 'event', 'course', 'created_at', 'updated_at']
    list_filter = ['event']


@admin.register(models.Assignment)
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


admin.site.register(models.Respond)
