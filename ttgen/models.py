# timetable/models.py

from django.db import models
from django.core.exceptions import ValidationError

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.IntegerField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TimetableEntry(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)  # e.g., Monday, Tuesday
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ('professor', 'day_of_week', 'start_time', 'end_time')

    def __str__(self):
        return f"{self.course} - {self.day_of_week} - {self.start_time}-{self.end_time}"

    def save(self, *args, **kwargs):
        # Find overlapping entries for the same professor
        overlapping_entries = TimetableEntry.objects.filter(
            professor=self.professor,
            day_of_week=self.day_of_week,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        ).exclude(id=self.id)

        # Check for conflicts
        if overlapping_entries.exists():
            raise ValidationError('This timetable entry conflicts with another entry for the same professor.')

        super().save(*args, **kwargs)
