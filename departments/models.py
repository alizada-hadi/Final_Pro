from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.template.defaultfilters import slugify


class Department(models.Model):
    DEPARTMENT_STATUS = (
        ("Lunched", "Lunched"),
        ("Lunching", "Lunching"),
        ("Not Available", "Not Available"),
    )
    dep_name = models.CharField(max_length=200)
    content = RichTextField(null=True, blank=True)
    dep_status = models.CharField(
        max_length=20, choices=DEPARTMENT_STATUS, default="Lunched")
    dep_publish_date = models.DateField()

    def __str__(self):
        return self.dep_name

    class Meta:
        # your custom permissions here
        pass


class Curriculum(models.Model):
    SEMESTER = (
        ("First", "First"),
        ("Second", "Second"),
        ("Third", "Third"),
        ("Fourth", "Fourth"),
        ("Fifth", "Fifth"),
        ("Sixth", "Sixth"),
        ("Seventh", "Seventh"),
        ("Eighth", "Eighth"),
    )
    CURRICULUM = (
        ("Bachelor", "Bachelor"),
        ("Master", "Master"),
    )
    CURRICULUM_TYPE = (
        ('Main', 'Main'),
        ('Secondary', 'Secondary'),
    )

    department = models.ForeignKey(
        Department, related_name="department", on_delete=models.CASCADE)
    curr_code = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    curr = models.CharField(
        max_length=20, choices=CURRICULUM, default="Bachelor")
    curr_name = models.CharField(max_length=200)
    curr_credit = models.IntegerField()
    curr_semester = models.CharField(
        max_length=20, choices=SEMESTER, default="First")
    curr_type = models.CharField(
        max_length=50, choices=CURRICULUM_TYPE, default="Main")

    curr_description = RichTextField()

    def __str__(self):
        return self.curr_name

    def get_absolute_url(self):
        return reverse('curriculum-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.curr_name)
        return super().save(*args, **kwargs)

    class Meta:
        # your custom permission goes here
        pass
