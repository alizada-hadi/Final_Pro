from django import forms
from django.forms import fields
from django.forms.models import modelformset_factory
from .models import Result
from courses.models import Course


class CreateResult(forms.Form):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all()
    )


EditResults = modelformset_factory(Result, fields=(
    "mid_term_exam",
    "final_exam",
    "project_score",
    "home_work_score",
    "class_activity_score",

),
    extra=0,
    can_delete=True)
