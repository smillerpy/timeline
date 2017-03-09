from rest_framework import serializers
from timeline.events.models import Event
from timeline.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'pk')

class EventSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Event
        fields = ('create_date', 'event_type', 'user')
