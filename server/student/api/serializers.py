from rest_framework import serializers
from student import models
from course.api import serializers as course_serializers


class StudentSerializer(serializers.ModelSerializer):
    courses = course_serializers.CourseSerializer(many=True, read_only=True)

    class Meta:
        model = models.Student
        fields = ('id', 'name', 'created_at', 'courses')
