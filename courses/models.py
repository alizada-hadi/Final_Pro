from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import User
from departments.models import Curriculum
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from students.models import Student
from django.utils import timezone


class Session(models.Model):
    SESSION_TYPE = (
        ("spring", "spring"),
        ("fall", "fall"),
    )
    session = models.DateField(default=timezone.now)
    session_type = models.CharField(
        max_length=20, choices=SESSION_TYPE, default="spring")

    def __str__(self):
        return f"{self.session_type} {self.session}"


class Course(models.Model):
    owner = models.ForeignKey(
        User, related_name="courses_created", on_delete=models.CASCADE)
    curriculum = models.ForeignKey(
        Curriculum, related_name="courses", on_delete=models.CASCADE)
    course_session = models.ForeignKey(
        Session, on_delete=models.CASCADE)
    students = models.ManyToManyField(
        Student, related_name="courses_joined", blank=True)
    code = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    overview = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visited_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass
        # your custom permissions

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Module(models.Model):
    course = models.ForeignKey(
        Course, related_name="modules", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'


class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE,
        limit_choices_to={
            "model__in": ('text', "video", "image", "file")
        }
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey("content_type", "object_id")
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    owner = models.ForeignKey(
        User, related_name="%(class)s_related", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def render(self):
        return render_to_string(f'courses/content/{self._meta.model_name}.html', {'item': self})

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = RichTextUploadingField(blank=True)


class File(ItemBase):
    content = RichTextUploadingField(blank=True)


class Image(ItemBase):
    content = RichTextUploadingField(blank=True)


class Video(ItemBase):
    content = RichTextUploadingField(blank=True)
