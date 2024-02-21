import base64
from rest_framework import serializers

from django.core.files.base import ContentFile
from djoser.serializers import UserCreateSerializer

from events.models import Event
from chat.models import Message, Room
from organizations.models import Organization
from users.models import User




class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'title',
            'description',
            'address',
            'postcode',
        )


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )


class UserChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class MessageSerializer(serializers.ModelSerializer):
    created_at_formatted = serializers.SerializerMethodField()
    user = UserChatSerializer()

    class Meta:
        model = Message
        exclude = []
        depth = 1

    def get_created_at_formatted(self, obj: Message):
        return obj.created_at.strftime('%d-%m-%Y %H:%M:%S')


class RoomSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = [
            'pk',
            'name',
            'host',
            'messages',
            'current_users',
            'last_message',
        ]
        depth = 1
        read_only_fields = ['messages', 'last_message']

    def get_last_message(self, obj: Room):
        return MessageSerializer(
            obj.messages.order_by('created_at').last()
        ).data
