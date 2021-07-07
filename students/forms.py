from django import forms
from accounts.models import User
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import Group
from departments.models import Department


class StudentSignUpForm(UserCreationForm):
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
    GENDER = (
        ('Male', 'male'),
        ('Female', 'female'),
    )
    kankor_id = forms.CharField(max_length=200, required=True)
    first_name = forms.CharField(max_length=200, required=True)
    father_name = forms.CharField(max_length=200, required=True)
    grand_father_name = forms.CharField(max_length=200, required=True)
    school_name = forms.CharField(max_length=200, required=True)
    score = forms.IntegerField(required=True)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    province = forms.CharField(max_length=200, required=True)
    gender = forms.ChoiceField(choices=GENDER)
    semester = forms.ChoiceField(choices=SEMESTER)
    section = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    kankor_exam_date = forms.DateField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'username', 'first_name',
                  'last_name', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        cleaned_data = super(StudentSignUpForm, self).clean()
        kankor_id = cleaned_data.get("kankor_id")
        first_name = cleaned_data.get("first_name")
        father_name = cleaned_data.get("father_name")
        grand_father_name = cleaned_data.get("grand_father_name")
        school_name = cleaned_data.get("school_name")
        score = cleaned_data.get("score")
        department = cleaned_data.get("department")
        province = cleaned_data.get("province")
        gender = cleaned_data.get("gender")
        semester = cleaned_data.get("semester")
        section = cleaned_data.get("section")
        last_name = cleaned_data.get("last_name")
        kankor_exam_date = cleaned_data.get("kankor_exam_date")

        user = super().save(commit=False)
        user.is_student = True
        # Group.objects.get(name="students").user_set.add(user)
        user.save()
        user.groups.add(Group.objects.get(name='students'))
        student = Student.objects.create(
            user=user,
            kankor_id=kankor_id,
            first_name=first_name,
            father_name=father_name,
            grand_father_name=grand_father_name,
            school_name=school_name,
            score=score,
            department=department,
            province=province,
            gender=gender,
            semester=semester,
            section=section,
            last_name=last_name,
            kankor_exam_date=kankor_exam_date
        )

        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            "cart",
            'cart_number',
            "page_number",
            "register_number",
            "volume",
            "cart_photo",
            "hostle",
            'wing_number',
            "room_number",
            "dob",
            "graduation_date_school",
            "interests",
            "rel_with_std",
            "name",
            "job",
            "phone1",
            "phone2",
            "address",
            "avatar",
        )
