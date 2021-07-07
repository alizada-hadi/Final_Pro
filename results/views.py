import results
from results.models import Result
from django.shortcuts import redirect, render
from .forms import CreateResult, EditResults
from django.contrib.auth.decorators import login_required
from students.models import Student
from courses.models import Course


@login_required
def create_result(request, pk):
    course = Course.objects.get(pk=pk)
    all_students = course.students.all()
    results = []
    if request.method == "POST":
        for s in all_students:
            results.append(
                Result(
                    course=course,
                    student=s
                )
            )
        Result.objects.bulk_create(results)
        return redirect("update-result", course.pk)
    return render(request, 'results/create_result.html', {
        "all_students": all_students,
        "course": course
    })


def edit_result(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == "POST":
        form = EditResults(request.POST)
        if form.is_valid():
            form.save()
            return redirect("update-result", course.pk)
    else:
        results = Result.objects.filter(course=course)
        form = EditResults(queryset=results)
    return render(request, "results/edit_result.html", {"formset": form})


def all_result_view(request, pk):
    course = Course.objects.get(pk=pk)
    results = Result.objects.filter(course=course)
    context = {
        "results": results
    }
    return render(request, "results/all_result.html", context)
