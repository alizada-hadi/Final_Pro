from ckeditor import fields
from django import forms
from .models import Course, Module
from django.forms.models import inlineformset_factory


ModuleFormSet = inlineformset_factory(
    Course,
    Module,
    fields=['title', 'content'],
    extra=1,
    can_delete=True
)
