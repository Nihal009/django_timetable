# timetable/pdf_utils.py

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import TimetableEntry
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    HTML(string=html).write_pdf(result)
    return HttpResponse(result.getvalue(), content_type='application/pdf')

def generate_pdf_timetable():
    timetable_by_year = {}
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    for year in range(1, 5):
        entries = TimetableEntry.objects.filter(course__year=year).order_by('day_of_week', 'start_time')
        timetable_by_year[year] = entries

    context = {
        'timetable_by_year': timetable_by_year,
        'days_of_week': days_of_week,
    }

    pdf = render_to_pdf('ttgen/timetable_pdf.html', context)
    return pdf
