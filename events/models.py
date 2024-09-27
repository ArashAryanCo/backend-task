from django.db import models
from django.core.exceptions import ValidationError

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    max_attendees = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def clean(self):
        if self.max_attendees <= 0:
            raise ValidationError('Max attendees must be greater than zero.')

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    event = models.ForeignKey(Event, related_name='tickets', on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, related_name='tickets', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['event', 'attendee']  # Ensure one attendee per event
