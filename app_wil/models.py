from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

# Create your models here.
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
    EXCUSES_CHOICES = (
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
    profile = models.ForeignKey(UserProfile, related_name="tardy_set")
    tardy_datetime = models.DateTimeField(default=datetime.now())
    period = models.CharField(max_length=100, choices=PERIOD_CHOICES)
    assessment = models.CharField(max_length=100)
    correct = models.BooleanField()
    level = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Tardies"
    
    def __str__(self):
        return "Attempt %s %s %s/%s/%s/%s" % (self.profile.user.username, self.attempt_datetime, self.level, self.assessment, self.word, self.correct)

    @property
    def time(self):
        return self.attempt_datetime.strftime('%I:%M:%S %P')

    @property
    def date(self):
        return self.attempt_datetime.strftime('%m/%d/%Y')

