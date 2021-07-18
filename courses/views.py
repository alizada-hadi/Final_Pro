from django.views.generic.edit import FormMixin
from events.forms import RespondForm
from .forms import AssignmentForm
from .models import Assignment
import datetime
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin,  View
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView
)
from .models import Course, Module, Content
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from .forms import ModuleFormSet
from django.forms.models import ModelForm, modelform_factory
from django.apps import apps
from departments.models import Curriculum
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from students.decorators import student_required
from django.core.exceptions import PermissionDenied
# mixins for course views


class GroupRequiredMixin(object):
    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        else:
            user_groups = []

            for group in request.user.groups.values_list("name", flat=True):
                user_groups.append(group)
            if len(set(user_groups).intersection(self.group_required)) <= 0:
                raise PermissionDenied

        return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)


class OwnerMixin(object):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin, GroupRequiredMixin):
    group_required = ["Instructor"]
    model = Course
    fields = ["curriculum", "code", "course_session", "title", "overview"]
    success_url = reverse_lazy("/")


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = "courses/form.html"


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'courses/list.html'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    success_url = reverse_lazy("course-list")


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    success_url = reverse_lazy("course-list")


class CourseDeleteView(OwnerCourseEditMixin,  DeleteView):
    template_name = "courses/course_confirm_delete.html"
    success_url = reverse_lazy("course-list")


# course module

class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = "courses/modules/formset.html"
    course = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course, data=data)

    def dispatch(self, request, pk):
        self.course = get_object_or_404(Course, id=pk, owner=request.user)

        return super().dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({
            'course': self.course,
            "formset": formset
        })

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("course-list")
        return self.render_to_response({
            "course": self.course,
            "formset": formset
        })


# course content view


class CourseContentCreateUpdateView(TemplateResponseMixin, View):
    module = None
    model = None
    obj = None
    template_name = "courses/content/form.html"

    def get_model(self, model_name):
        if model_name in ['text', 'video', 'image', 'file']:
            return apps.get_model(app_label='courses', model_name=model_name)
        return None

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['owner',
                                                 'order',
                                                 'created_at',
                                                 'updated_at'])
        return Form(*args, **kwargs)

    def dispatch(self, request, module_id, model_name, id=None):
        self.module = get_object_or_404(
            Module, id=module_id, course__owner=request.user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model, id=id, owner=request.user)
        return super().dispatch(request, module_id, model_name, id)

    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({'form': form, 'object': self.obj})

    def post(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj,
                             data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            if not id:
                Content.objects.create(module=self.module, item=obj)
            return redirect('module_content_list', self.module.id)
        return self.render_to_response({'form': form, 'object': self.obj})


class ContentDeleteView(View):
    def post(self, request, id):
        content = get_object_or_404(
            Content, id=id, module__course__owner=request.user)
        module = content.module
        content.item.delete()

        return redirect("module_content_list", module.id)


class ModuleContentListView(TemplateResponseMixin, View):
    template_name = 'courses/content/content_list.html'

    def get(self, request, module_id):
        module = get_object_or_404(
            Module, id=module_id, course__owner=request.user)

        return self.render_to_response({"module": module})


class CourseListView(TemplateResponseMixin, View):
    model = Course
    template_name = "courses/course/list.html"

    def get(self, request, curriculum=None):
        curriculums = Curriculum.objects.filter(
            curr_semester=request.user.student.semester
        ).annotate(
            total_courses=Count("courses")
        )
        courses = Course.objects.annotate(
            total_modules=Count("modules")
        )
        today = datetime.date.today

        if curriculum:
            curriculum = get_object_or_404(Curriculum, slug=curriculum)
            courses = courses.filter(curriculum=curriculum)

        return self.render_to_response({
            "curriculums": curriculums,
            "curriculum": curriculum,
            "courses": courses,
            "today": today
        })


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course/detail.html"


@login_required
@student_required
def join_course_view(request, slug):
    course = Course.objects.get(slug=slug)
    if request.method == "POST":
        code = request.POST.get("join_code")
        if code == course.code:
            course.students.add(request.user.student)
        return redirect("student-course-list")
    return render(request, "courses/join.html")


# assignment views

class AssignmentCreateView(CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'courses/assignment/form.html'

    success_url = reverse_lazy("")

    def get_context_data(self, **kwargs):
        context = super(AssignmentCreateView, self).get_context_data(**kwargs)
        context["form"] = AssignmentForm(
            initial={"owner": self.request.user.staff,
                     "content": Content.objects.get(pk=self.kwargs.get("pk"))}
        )
        return context


class AssignmentDetailView(FormMixin, DetailView):
    model = Assignment
    template_name = "courses/assignment/assignment_detail.html"
    form_class = RespondForm
    success_url = reverse_lazy("")

    def get_context_data(self, **kwargs):
        context = super(AssignmentDetailView, self).get_context_data(**kwargs)
        context["form"] = RespondForm(
            initial={"assignment": self.object, "student": self.request.user.student.pk})
        print(context["form"])
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(AssignmentDetailView, self).form_valid(form)
