from rest_framework import viewsets
from student.api import serializers
from student import models


class StudentViewSet(viewsets.ModelViewSet):
   serializer_class = serializers.StudentSerializer
   queryset = models.Student.objects.all()
