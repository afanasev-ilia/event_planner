from rest_framework import mixins, viewsets

from api.serializers import OrganizationSerializer, EventSerializer
from organizations.models import Organization
from events.models import Event


class EventCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class OrganizationCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
