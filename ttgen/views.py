# timetable/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .scheduler import generate_timetable
from .models import TimetableEntry
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def generate_timetable_view(request):
    generate_timetable()
    return redirect('index')

def index(request):
    entries = TimetableEntry.objects.all().order_by('day_of_week', 'start_time', 'professor')
    timetable_by_year = {}
    for entry in entries:
        year = entry.course.year
        if year not in timetable_by_year:
            timetable_by_year[year] = []
        timetable_by_year[year].append(entry)
    return render(request, 'timetable/index.html', {'timetable_by_year': timetable_by_year})

def generate_pdf(request):
    entries = TimetableEntry.objects.all().order_by('day_of_week', 'start_time', 'professor')
    timetable_by_year = {}
    for entry in entries:
        year = entry.course.year
        if year not in timetable_by_year:
            timetable_by_year[year] = []
        timetable_by_year[year].append(entry)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="timetable.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []

    for year, entries in timetable_by_year.items():
        elements.append(Table([[f"Year {year}"]], colWidths=[500], hAlign='CENTER'))
        elements.append(Table([["Course", "Professor", "Day of Week", "Start Time", "End Time"]], colWidths=[100, 100, 100, 100, 100], style=[('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), ('BOTTOMPADDING', (0, 0), (-1, 0), 12), ('BACKGROUND', (0, 1), (-1, -1), colors.beige), ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

        for entry in entries:
            elements.append(Table([[entry.course.name, entry.professor.name, entry.day_of_week, entry.start_time, entry.end_time]], colWidths=[100, 100, 100, 100, 100], style=[('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'), ('BOTTOMPADDING', (0, 0), (-1, -1), 12), ('BACKGROUND', (0, 0), (-1, -1), colors.whitesmoke if entries.index(entry) % 2 == 0 else colors.lightgrey)]))

        elements.append(Table([[""]], colWidths=[500], style=[('BACKGROUND', (0, 0), (-1, 0), colors.white)]))  # Add spacing between years

    doc.build(elements)
    return response
