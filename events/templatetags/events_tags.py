from django.db.models import Count
from django import template
from ..models import Respond, Assignment
register = template.Library()


@register.simple_tag
def student_submissions(request, assignment):
    return Respond.objects.filter(student=request.user.student, assignment=assignment).count()


@register.simple_tag
def submission_status(request, assignment):
    number_of_respond = Respond.objects.filter(
        student=request.user.student, assignment=assignment).count()
    status = "Not Submitted"
    if number_of_respond > 0:
        status = "Submitted"
    return status
