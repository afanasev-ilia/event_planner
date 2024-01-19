from rest_framework import serializers

from djoser.serializers import UserCreateSerializer

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
