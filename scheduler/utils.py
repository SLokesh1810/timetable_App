import random
from datetime import date
from .models import Batch, Subject, Timeslots, Timetable, TimetableEntry, Room

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def generate_timetable(batch_id, start_date=date.today()):
    batch = Batch.objects.get(id=batch_id)

    # --- create (or bump) timetable version ---
    latest_version = Timetable.objects.filter(batch=batch).count() + 1
    timetable = Timetable.objects.create(
        batch=batch, version=latest_version, start_date=start_date, is_active=True
    )

    # pull subjects & slots
    subjects = list(Subject.objects.all())
    slots    = list(Timeslots.objects.all())

    # very naive distribution (replace later with smarter logic)
    for day in DAYS:
        day_subjects = random.sample(subjects, len(slots))
        for slot, subject in zip(slots, day_subjects):
            TimetableEntry.objects.create(
                timetable=timetable,
                day_of_week=day,
                slot=slot,
                subject=subject,
                room=random.choice(list(Room.objects.all())),
                is_locked=False
            )
    return timetable
