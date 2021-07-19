import os
import csv
from io import StringIO
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Curriculum, CurriculumUploadList, Department


@receiver(post_save, sender=CurriculumUploadList)
def create_bulk_curriculum(sender, created, instance, *args, **kwargs):
    if created:
        opened = StringIO(instance.csv_file.read().decode())
        reading = csv.DictReader(opened, delimiter=",")
        curriculums = []

        for row in reading:
            if 'curr_code' in row and row["curr_code"]:
                curr_code = row["curr_code"]
                department = row["department"] if 'department' in row and row["department"] else ""
                curr = row["curr"] if 'curr' in row and row["curr"] else ""
                curr_name = row["curr_name"] if 'curr_name' in row and row["curr_name"] else ""
                curr_credit = row["curr_credit"] if 'curr_credit' in row and row["curr_credit"] else ""
                curr_semester = row["curr_semester"] if 'curr_semester' in row and row["curr_semester"] else ""
                curr_type = row["curr_type"] if 'curr_type' in row and row["curr_type"] else ""
                curr_description = row["curr_description"] if 'curr_description' in row and row["curr_description"] else ""
                if department:
                    dep, kind = Department.objects.get_or_create(
                        dep_name=department)
                check = Curriculum.objects.filter(
                    curr_code=curr_code).exists()
                if not check:
                    curriculums.append(
                        Curriculum(
                            department=dep,
                            curr_code=curr_code,
                            curr=curr,
                            curr_name=curr_name,
                            curr_credit=curr_credit,
                            curr_semester=curr_semester,
                            curr_type=curr_type,
                            curr_description=curr_description
                        )
                    )
        Curriculum.objects.bulk_create(curriculums)
        instance.csv_file.close()
        instance.delete()
