from rest_framework import serializers

from course.models import Course
from student.models import Student
from rest_framework.response import Response


class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Student
        fields = ('id', 'name', 'created_at', 'courses')

    def create(self, validated_data):
        courses_data = validated_data.pop('courses', [])
        student = Student.objects.create(**validated_data)
        for course_data in courses_data:
            course = Course.objects.create(**course_data)
            student.courses.add(course)
        return student

    def partial_update(self, request):
        instance = self.get_object()
        courses = request.data.get('courses', None)

        if courses is not None:
            instance.courses.clear()

            for course_id in courses:
                try:
                    course = Course.objects.get(id=course_id)
                    instance.courses.add(course)
                except Course.DoesNotExist:
                    pass

            instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
