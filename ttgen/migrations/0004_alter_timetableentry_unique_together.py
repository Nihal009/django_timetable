# Generated by Django 5.0.7 on 2024-07-19 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttgen', '0003_alter_course_professor'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='timetableentry',
            unique_together={('professor', 'day_of_week', 'start_time', 'end_time')},
        ),
    ]
