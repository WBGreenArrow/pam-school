# Generated by Django 3.2.8 on 2023-05-25 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='create_at',
            new_name='created_at',
        ),
    ]