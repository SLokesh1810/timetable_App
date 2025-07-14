from django.shortcuts import render
from .models import Timetable, Batch, TimetableEntry, Timeslots

def welcome_view(request):
    return render(request, 'welcome.html')

