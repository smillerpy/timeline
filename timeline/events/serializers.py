from rest_framework import serializers
from timeline.events.models import Event, CoolEvent, SuperCoolEvent
from timeline.events import constants 
from timeline.users.models import User
from timeline.common.models import Registrator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'pk')

class EventSerializer(serializers.ModelSerializer, Registrator):
    user = UserSerializer()
    class Meta:
        model = Event
        fields = ('create_date', 'event_type', 'user')

    def to_representation(self, obj):
        data = super(EventSerializer, self).to_representation(obj)
        fullobj = obj.get_full_event()
        serializer = self.get_cls_by_type(obj.event_type)()
        data.update(serializer.to_representation(fullobj))
        return data

    #def to_internal_value(self, data)

@EventSerializer.register(constants.COOL_EVENT)
class CoolEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoolEvent
        fields = ('link', 'color')

@EventSerializer.register(constants.SUPERCOOL_EVENT)
class SuperCoolEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperCoolEvent
        fields = ('description', )




