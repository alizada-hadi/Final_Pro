from django.db import models
from students.models import Student
from courses.models import Course


class Result(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mid_term_exam = models.IntegerField(default=0)
    final_exam = models.IntegerField(default=0)
    project_score = models.IntegerField(default=0)
    home_work_score = models.IntegerField(default=0)
    class_activity_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student}'s {self.course} score "

    def total(self):
        return self.final_exam + self.project_score + self.home_work_score + self.class_activity_score + self.mid_term_exam

    def total_score(self):
        return self.mid_term_exam + self.final_exam + self.project_score + self.home_work_score + self.class_activity_score
