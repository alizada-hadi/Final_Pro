from django.forms import ModelForm, DateInput
from django import forms
from .models import EventMember, Event
from courses.models import Course
from django_select2 import forms as s2forms


class CourseWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        'title__icontains',
        'slug__icontains',
    ]


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'course', 'start_time', 'end_time']
        widgets = {
            "course": CourseWidget,
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter event title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter event description'
            }),
            'start_time': DateInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'end_time': DateInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
        }
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields["course"].queryset = Course.objects.filter(
            owner=self.user)


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ['course']
