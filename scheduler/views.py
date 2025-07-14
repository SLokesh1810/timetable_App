from django.shortcuts import render
from .models import Timetable, Batch, TimetableEntry, Timeslots
from .utils import generate_timetable

def timetable_view(request):
    batch_id = 1  # later this can come from a dropdown or login
    batch = Batch.objects.get(id=batch_id)

    # Get or generate timetable
    timetable = Timetable.objects.filter(batch=batch, is_active=True).first()
    if not timetable:
        timetable = generate_timetable(batch_id)

    entries = TimetableEntry.objects.filter(timetable=timetable)
    slots = Timeslots.objects.all().order_by("start_time")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # Structure data as {day: {slot_id: entry}}
    timetable_data = {day: {} for day in days}
    for entry in entries:
        timetable_data[entry.day_of_week][entry.slot.id] = entry

    return render(request, 'timetable.html', {
        'timetable': timetable,
        'slots': slots,
        'days': days,
        'timetable_data': timetable_data
    })
