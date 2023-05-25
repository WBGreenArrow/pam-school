from rest_framework import viewsets
from course.api.serializers import CourseSerializer
from course.models import Course


class CourseViewSet(viewsets.ModelViewSet):
   queryset = Course.objects.all()
   serializer_class = CourseSerializer
