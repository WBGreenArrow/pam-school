from django.db import models
from uuid import uuid4
from course import models as course_model
# Create your models here.


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    courses = models.ManyToManyField(course_model.Course, related_name='enrolled_students')

    def __str__(self):
        return self.name

    def get_courses_with_details(self):
        return self.courses.all().values('id', 'name', 'description')

