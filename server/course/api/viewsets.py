from rest_framework import viewsets
from course.api import serializers
from course import models


class CourseViewSet(viewsets.ModelViewSet):
   serializer_class = serializers.CourseSerializer
   queryset = models.Course.objects.all()
