# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import


from timeline.common.models import Registrator
from timeline.events import constants
from timeline.users.models import User

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class Event(models.Model, Registrator):
    create_date = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(verbose_name=_("Event Type"), max_length=2, choices=constants.EVENT_TYPES)
    user =  models.ForeignKey(User())

    def get_type_name(self):
        return constants.EVENT_TYPES_DICT[self.get_type()]

    def __unicode__(self):
        return u"%s (%s)" % (self.__class__, self.pk)

    def get_full_event(self):
        model = self.get_cls_by_type(self.event_type)
        e = model.objects.get(pk=self.id)
        return e

    def get_cls_type(self):
        return self.__class__.get_type()

    @classmethod
    def get_type(cls):
        raise NotImplemented

    def get_template(self):
        raise NotImplemented

    def get_badge(self):
        raise NotImplemented

@Event.register(constants.COOL_EVENT)
class CoolEvent(Event):
    link = models.URLField(max_length=200)
    color = models.CharField(max_length=6)

    def __init__(self, *args, **kwargs):
        super(CoolEvent, self).__init__(*args, **kwargs)
        self.event_type = CoolEvent.get_type()

    @classmethod
    def get_type(cls):
        return constants.COOL_EVENT

    def get_template(self):
        return "event_cool"

    def get_badge(self):
        return "thumbs-o-up"

@Event.register(constants.SUPERCOOL_EVENT)
class SuperCoolEvent(Event):
    description = models.CharField(max_length=150)

    def __init__(self, *args, **kwargs):
        super(SuperCoolEvent, self).__init__(*args, **kwargs)
        self.event_type = SuperCoolEvent.get_type()

    @classmethod
    def get_type(cls):
        return constants.SUPERCOOL_EVENT

    def get_template(self):
        return "event_supercool"

    def get_badge(self):
        return "snowflake-o"
