# timetable/scheduler.py

from datetime import time
from .models import Course, TimetableEntry

DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def generate_timetable():
    TimetableEntry.objects.all().delete()  # Clear existing entries

    start_times = [time(9, 0), time(10, 0), time(11, 0), time(12, 0), time(14, 0), time(15, 0), time(16, 0)]
    end_times = [time(10, 0), time(11, 0), time(12, 0), time(13, 0), time(15, 0), time(16, 0), time(17, 0)]

    for year in range(1, 5):
        courses = Course.objects.filter(year=year)
        course_idx = 0
        for day in DAYS_OF_WEEK:
            for start_time, end_time in zip(start_times, end_times):
                if course_idx < len(courses):
                    course = courses[course_idx]
                    # Ensure the professor doesn't have a conflict
                    if not TimetableEntry.objects.filter(
                            professor=course.professor,
                            day_of_week=day,
                            start_time__lt=end_time,
                            end_time__gt=start_time).exists():
                        TimetableEntry.objects.create(
                            course=course,
                            professor=course.professor,
                            day_of_week=day,
                            start_time=start_time,
                            end_time=end_time
                        )
                        course_idx += 1
