# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render

from rest_framework import viewsets
from timeline.events.serializers import EventSerializer, UserSerializer
from timeline.events.models import Event
from timeline.users.models import User

class UserViewSet(viewsets.ModelViewSet):
    """
        Users to ve seen or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
        events to ve seen or edited
    """
    queryset = Event.objects.all().order_by('-create_date')
    serializer_class = EventSerializer

def events(request):
    return render(request, 'events/events.html')
