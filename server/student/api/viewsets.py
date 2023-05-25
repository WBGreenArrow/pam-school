from rest_framework import viewsets
from student.api.serializers import StudentSerializer
from student.models import Student


class StudentViewSet(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer

