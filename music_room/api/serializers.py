from rest_framework import serializers

from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    """ Room Serializer """
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')
