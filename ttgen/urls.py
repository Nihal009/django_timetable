# timetable/urls.py

from django.urls import path
from .views import timetable_view ,generate_pdf_view

urlpatterns = [
   # path('generate/', generate_timetable_view, name='generate'),
    path('generate_pdf/', generate_pdf_view, name='generate_pdf'),
    path('',timetable_view, name='timetable'),
]
