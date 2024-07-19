# timetable/management/commands/clear_db.py

from django.core.management.base import BaseCommand
from ttgen.models import Department, Professor, Course, TimetableEntry

class Command(BaseCommand):
    help = 'Clears the database'

    def handle(self, *args, **kwargs):
        TimetableEntry.objects.all().delete()
        Course.objects.all().delete()
        Professor.objects.all().delete()
        Department.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Database cleared successfully!'))
