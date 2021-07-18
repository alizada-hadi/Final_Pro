from .models import Assignment
from ckeditor import fields
from django.forms import DateInput
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


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['owner', 'title', 'body',
                  'avalibality', 'content', 'due_date']

        widgets = {

            "due_date": DateInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            "owner": forms.HiddenInput(),
            "content": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AssignmentForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['due_date'].input_formats = ('%Y-%m-%dT%H:%M',)
