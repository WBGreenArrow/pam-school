from django.db import models
from uuid import uuid4
# Create your models here.


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)