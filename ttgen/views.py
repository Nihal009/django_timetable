# timetable/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .scheduler import generate_timetable
from .pdf_utils import generate_pdf_timetable
from .models import TimetableEntry

DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def timetable_view(request):
    generate_timetable()

    timetable_by_year = {}
    for year in range(1, 5):
        entries = TimetableEntry.objects.filter(course__year=year).order_by('day_of_week', 'start_time')
        timetable_by_year[year] = entries

    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return render(request, 'ttgen/timetable.html', {
        'timetable_by_year': timetable_by_year,
        'days_of_week': days_of_week
    })

def generate_pdf_view(request):
    pdf = generate_pdf_timetable()
    return HttpResponse(pdf, content_type='application/pdf')
