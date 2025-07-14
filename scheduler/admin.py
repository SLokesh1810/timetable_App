from django.contrib import admin
from .models import Batch, Subject, Timeslots, Room, Timetable, TimetableEntry

# Register your models here.

admin.site.register(Batch)
admin.site.register(Subject)
admin.site.register(Timeslots)
admin.site.register(Room)
admin.site.register(Timetable)
admin.site.register(TimetableEntry)
