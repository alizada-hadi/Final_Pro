from datetime import datetime
from students.models import Student
from courses.models import Course
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, request
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta, datetime, date
import calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

# Create your views here.
from .forms import EventForm, AddMemberForm, RespondForm
from .utils import Calendar
from .models import Event, EventMember, Respond
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from staff.decorators import staff_required
from django.views.generic.edit import FormMixin
from courses.models import Assignment


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


@method_decorator([login_required, staff_required], name="dispatch")
class EventCreateView(generic.CreateView):
    model = Event
    form_class = EventForm
    template_name = "events/event_form.html"
    success_url = reverse_lazy("calendar")

    def form_valid(self, form):
        event = form.save(commit=False)
        event.user = self.request.user
        return super(EventCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(EventCreateView,  self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


def check_assignment_view(reqeust, slug):
    std = Student.objects.all()
    assignment = Assignment.objects.get(slug=slug)

    responds = Respond.objects.filter(assignment=assignment)
    number_of_respond = Respond.objects.filter(assignment=assignment).count()
    # unrespond = number_of_students - number_of_respond
    context = {
        "assignment": assignment,
        "responds": responds,
        "number_of_respond": number_of_respond,
        # "number_of_students": number_of_students,
        # "students": students,
        # "unrespond": unrespond
    }
    return render(reqeust, "events/respond_list.html", context)


def respond_detail(request, pk):
    respond = Respond.objects.get(pk=pk)
    context = {
        "respond": respond
    }
    return render(request, "events/respond_detail.html", context)


class EventEdit(generic.UpdateView):
    model = Event
    fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'event.html'


def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    eventmember = EventMember.objects.filter(event=event)
    context = {
        'event': event,
        'eventmember': eventmember
    }
    return render(request, 'event-details.html', context)


def add_eventmember(request, event_id):
    forms = AddMemberForm()
    if request.method == 'POST':
        forms = AddMemberForm(request.POST)
        if forms.is_valid():
            member = EventMember.objects.filter(event=event_id)
            event = Event.objects.get(id=event_id)
            if member.count() <= 9:
                course = forms.cleaned_data['course']
                EventMember.objects.create(
                    event=event,
                    course=course
                )
                return redirect('calendarapp:calendar')
            else:
                print('--------------User limit exceed!-----------------')
    context = {
        'form': forms
    }
    return render(request, 'add_member.html', context)


class EventMemberDeleteView(generic.DeleteView):
    model = EventMember
    template_name = 'event_delete.html'
    success_url = reverse_lazy('calendarapp:calendar')


class CalendarViewNew(LoginRequiredMixin, generic.View):
    template_name = 'events/calendar.html'
    form_class = EventForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        events = Event.objects.get_all_events(user=request.user)
        events_month = Event.objects.get_running_events(user=request.user)
        # my_courses = Course.objects.filter(students__in=[request.user.student])
        event_list = []
        # start: '2020-09-16T16:00:00'
        for event in events:
            event_list.append({
                'title': event.title,
                'start': event.start_time.date().strftime("%Y-%m-%dT%H:%M:%S"),
                'end': event.end_time.date().strftime("%Y-%m-%dT%H:%M:%S"),
            })
        context = {
            'form': forms,
            'events': event_list,
            'events_month': events_month,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('calendar')
        context = {
            'form': forms
        }
        return render(request, self.template_name, context)


class StudentCalenderListView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'events/student_calendar.html'

    def get_context_data(self, *args, **kwargs):
        context = super(StudentCalenderListView,
                        self).get_context_data(**kwargs)
        context["events"] = Event.objects.all()

        return context
