from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db.models import Count
from .models import Event, Attendee, Ticket
from .serializers import EventSerializer, AttendeeSerializer, TicketSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().prefetch_related('tickets__attendee')
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        max_attendees = request.data.get('max_attendees')
        if int(max_attendees) <= 0:
            raise ValidationError('Max attendees must be greater than zero.')
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().select_related()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().select_related('event', 'attendee')
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        event_id = request.data.get('event')
        event = Event.objects.get(id=event_id)
        attendee_count = event.tickets.count()

        if attendee_count >= event.max_attendees:
            raise ValidationError('Event has reached max attendees.')
        return super().create(request, *args, **kwargs)
