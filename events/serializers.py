from rest_framework import serializers
from .models import Event, Attendee, Ticket

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['id', 'name', 'email']

class EventSerializer(serializers.ModelSerializer):
    attendees = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'date', 'location', 'max_attendees', 'attendees']

    def get_attendees(self, obj):
        tickets = obj.tickets.all()
        attendees = [ticket.attendee for ticket in tickets]
        return AttendeeSerializer(attendees, many=True).data

    def validate_max_attendees(self, value):
        if value <= 0:
            raise serializers.ValidationError('Max attendees must be greater than zero.')
        return value

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'event', 'attendee']
