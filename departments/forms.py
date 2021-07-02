from django import forms
from django.forms import fields
from .models import Department, Curriculum


class DepForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = (
            "dep_name",
            "content",
            "dep_status",
            "dep_publish_date",
        )


class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = (
            'department',
            "curr_code",
            "curr_name",
            "curr",
            "curr_credit",
            "curr_semester",
            "curr_type",
            "curr_description",
        )
