from django.db import models
from accounts.models import User
from departments.models import Department


class Staff(models.Model):
    STATUS = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )
    CART = (
        ('paper', 'paper'),
        ('electric', 'electric'),
    )
    GENDER = (
        ("مرد", "male",),
        ("زن", "female"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=GENDER, default="مرد")
    dob = models.DateField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    national_cart = models.CharField(
        max_length=20, choices=CART, default="electric")
    cart_number = models.CharField(max_length=255)
    page_number = models.IntegerField(null=True, blank=True)
    register_number = models.IntegerField(null=True, blank=True)
    volume = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    cart_image = models.ImageField(
        upload_to="staff/images", default="cart.jpg")
    address = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="active")
    avatar = models.ImageField(upload_to="staff/images", null=True, blank=True)

    def __str__(self):
        return self.first_name


class StaffEducation(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    edu_title = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    diploma = models.ImageField(
        upload_to="staff/edu/images", null=True, blank=True)

    def __str__(self):
        return self.edu_title


class StaffJobExp(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, null=True, blank=True)
    salary = models.DecimalField(
        max_digits=10, decimal_places=1, null=True, blank=True)
    duration = models.CharField(max_length=200, null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    approve_letter = models.ImageField(
        upload_to="staff/job/images", null=True, blank=True)

    def __str__(self):
        return self.job_title
