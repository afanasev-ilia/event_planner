import base64
from rest_framework import serializers

from django.core.files.base import ContentFile
from djoser.serializers import UserCreateSerializer

from events.models import Event
from organizations.models import Organization
from users.models import User


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)


class OrganizationEventSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True, many=True)
    organizations_details = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ('title', 'organizations_details', 'employee')
 
    def get_organizations_details(self, obj):
        return f'{obj.postcode}, {obj.address}'


class EventSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=True, allow_null=False)
    organizations = OrganizationEventSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = (
            'title',
            'description',
            'organizations',
            'image',
            'date',
        )


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
