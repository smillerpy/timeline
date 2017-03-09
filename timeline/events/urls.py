# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

urlpatterns = [
    url(regex=r'^$',
        view='events.views.events',
        name="home"),
        ]
