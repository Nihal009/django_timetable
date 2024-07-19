# timetable/urls.py

from django.urls import path
from .views import generate_timetable_view, index, generate_pdf

urlpatterns = [
    path('generate/', generate_timetable_view, name='generate'),
    path('generate_pdf/', generate_pdf, name='generate_pdf'),
    path('', index, name='index'),
]
