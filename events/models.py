from students.models import Student
from django.template.defaultfilters import slugify
from django.db import models
from accounts.models import User
from courses.models import Course
from django.urls import reverse
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from staff.models import Staff


class EventAbstract(models.Model):
    """ Event abstract model """
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EventMember(EventAbstract):
    """ Event member model """
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['event', 'course']

    def __str__(self):
        return str(self.course)


class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self, user):
        events = Event.objects.filter(
            user=user, is_active=True, is_deleted=False
        )
        return events

    def get_running_events(self, user):
        running_events = Event.objects.filter(
            user=user, is_active=True, is_deleted=False,
            end_time__gte=datetime.now().date()
        ).order_by('start_time')
        return running_events


class Event(EventAbstract):
    """ Event model """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    objects = EventManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('event-detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


class Assignment(models.Model):
    instructor = models.ForeignKey(
        Staff, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    slug = models.SlugField(unique=True, null=False)
    assign_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    member = models.ManyToManyField(Course)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Respond(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    content = RichTextUploadingField()
