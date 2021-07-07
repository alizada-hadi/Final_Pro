from django.db import models
from accounts.models import User
from departments.models import Department
from django.utils.html import escape, mark_safe


class Student(models.Model):
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
    STATUS = (
        ('active', 'active'),
        ('chance', 'chance'),
        ('break', 'break'),
        ('nextYear', 'nextYear'),
        ('drop', 'drop'),
    )
    CART = (
        ('electric', 'electric'),
        ('paper', 'paper'),
    )
    GENDER = (
        ('Male', 'male'),
        ('Female', 'female'),
    )
    HOSTLE = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    # data comming from kankor form
    kankor_id = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    grand_father_name = models.CharField(max_length=200)
    school_name = models.CharField(max_length=200)
    score = models.IntegerField(default=300)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    province = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, default="male")
    semester = models.CharField(
        max_length=20, choices=SEMESTER, default='First')
    section = models.CharField(max_length=200, default="A")
    last_name = models.CharField(max_length=200)
    # data comming from existing students

    hostle = models.CharField(max_length=20, choices=HOSTLE, default='No')
    wing_number = models.IntegerField(default=1)
    room_number = models.IntegerField(default=100)

    # extra information

    dob = models.DateField(null=True, blank=True)
    graduation_date_school = models.DateField(null=True, blank=True)
    kankor_exam_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default="active")
    # student relative information
    name = models.CharField(max_length=200)
    rel_with_std = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=200)
    phone2 = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    # student interests
    interests = models.ManyToManyField(
        "InterestTopic", related_name="interested_students")

    # Identity cart information

    cart = models.CharField(max_length=100, choices=CART,
                            default='electric', null=True, blank=True)
    cart_number = models.CharField(
        max_length=200, unique=True, null=True, blank=True)
    page_number = models.IntegerField(null=True, blank=True)
    register_number = models.CharField(max_length=200, null=True, blank=True)
    volume = models.IntegerField(null=True, blank=True)

    cart_photo = models.ImageField(
        upload_to="images/students/cart", null=True, blank=True)

    # personal

    avatar = models.ImageField(
        upload_to="images/students/avatar", null=True, blank=True)

    class Meta:
        pass
        # your permissions here

    def __str__(self):
        return self.first_name


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

    @property
    def get_categories(self):
        return InterestTopic.objects.filter(category__category=self.category)


class InterestTopic(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=14, default='#007bff')

    def __str__(self):
        return self.title

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (
            color, name)
        return mark_safe(html)
