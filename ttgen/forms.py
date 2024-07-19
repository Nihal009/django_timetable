from django import forms
from .models import TimetableEntry

class TimetableEntryForm(forms.ModelForm):
    class Meta:
        model = TimetableEntry
        fields = ['course', 'professor', 'day_of_week', 'start_time', 'end_time']
