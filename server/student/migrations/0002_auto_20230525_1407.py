# Generated by Django 3.2.8 on 2023-05-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_rename_create_at_course_created_at'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(related_name='enrolled_students', to='course.Course'),
        ),
    ]
