from django import forms
from django.db.models import fields
from accounts.models import User
from departments.models import Department
from .models import Staff
from django.db import transaction
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm


class StaffSignUpForm(UserCreationForm):
    GENDER = (
        ("مرد", "male",),
        ("زن", "female"),
    )
    staff_id = forms.CharField(max_length=200, required=True)
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    father_name = forms.CharField(max_length=200, required=True)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    gender = forms.ChoiceField(choices=GENDER)
    group = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple,
                                           required=True
                                           )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    @transaction.atomic
    def save(self, commit=True):
        cleaned_data = super(StaffSignUpForm, self).clean()
        staff_id = cleaned_data.get('staff_id')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        father_name = cleaned_data.get('father_name')
        department = cleaned_data.get('department')
        gender = cleaned_data.get("gender")
        # group = cleaned_data.get("group")
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
            user.groups.add(*self.cleaned_data.get("group"))

        staff = Staff.objects.create(
            user=user,
            staff_id=staff_id,
            first_name=first_name,
            last_name=last_name,
            father_name=father_name,
            department=department,
            gender=gender,
        )

        return user


class StaffProfileDetailInfo(forms.ModelForm):
    class Meta:
        model = Staff
        fields = (
            "national_cart",
            "cart_number",
            "page_number",
            "register_number",
            "volume",
            "phone_number",
            "cart_image",
            "address",
            "status",
            "avatar"
        )


class StaffUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email"
        )
