from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Batch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"id: {self.id} - {self.name}"
    
class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=50, choices=[('Theory', 'Theory'),('Lab', 'Lab'),])
    hrs_per_week = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.code}) - {self.type})"
    
class Timeslots(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=50, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.label} : {self.start_time} - {self.end_time}"
    
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50, choices=[('Lecture', 'Lecture'), ('Lab', 'Lab')])

    def __str__(self):
        return f"{self.name} - {self.type}"
    
class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    version = models.IntegerField(default=1)
    start_date = models.DateField()
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.batch.name} - v{self.version}"
    
class TimetableEntry(models.Model):
    id = models.AutoField(primary_key=True)
    Timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(Timeslots, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')])
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject.name} - {self.timeslot.label} - {self.room.name} - {self.day}"