# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from rest_framework import routers
from timeline.events.views import events, EventViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^events/', include(router.urls)),
    url(regex=r'^$',
        view=events,
        name="home"),
        ]
