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
        return redirect("update-result")
    return render(request, 'results/create_result.html', {
        "all_students": all_students,
        "course": course
    })


def edit_result(request):
    if request.method == "POST":
        form = EditResults(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        results = Result.objects.all()
        form = EditResults(queryset=results)
    return render(request, "results/edit_result.html", {"formset": form})
