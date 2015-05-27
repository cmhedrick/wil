from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
import django.utils.timezone
		
class Tardy(models.Model):
    APPOINTMENT = "Appointment"
    D_APPOINTMENT = "Dentist Appointment"
    DR_APPOINTMENT = "Dr. Appointment"
    HOLIDAY = "Holiday"
    TESTING = "Testing"
    FAMILY = "Family"
    MEETING = "Meeting"
    MEETING_CHILD = "Meeting At Child's School"
    BUS = "Missed The Bus"
    SICK = "Sick (Headache, etc.)"
    WORK = "Work"
    OTHER = "Other"
    PERIOD_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    EXCUSE_CHOICES = (
        (APPOINTMENT, 'Appointment'),
        (D_APPOINTMENT, 'Dentist Appointment'),
        (DR_APPOINTMENT, 'Dr. Appointment'),
        (HOLIDAY, 'Holiday'),
        (TESTING, 'Testing'),
        (FAMILY, 'Family'),
        (MEETING, 'Meeting'),
        (MEETING_CHILD, 'Meeting At Child\'s School'),
        (BUS, 'Missed The Bus'),
        (SICK, 'Sick (Headache, etc.)'),
        (WORK, 'Work'),
        (OTHER, 'Other'),
    )
    tardy_datetime = models.DateTimeField(default=django.utils.timezone.now())
    period = models.CharField(max_length=100, choices=PERIOD_CHOICES)
    excuse = models.CharField(max_length=100, choices=EXCUSE_CHOICES)
    note = models.BooleanField()
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Tardies"
    
    def __str__(self):
        return "%s: %s" % (self.name, self.date)

    @property
    def time(self):
        return self.tardy_datetime.strftime('%I:%M:%S %P')

    @property
    def date(self):
        return self.tardy_datetime.strftime('%m/%d/%Y')

