from django.contrib import admin
from .models import Student, InterestTopic,  Category


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "kankor_id",
        "first_name",
        "last_name",
    )


@admin.register(InterestTopic)
class InterestAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "title",
        "color",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "category",
    )
