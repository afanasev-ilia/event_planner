from rest_framework import mixins, viewsets

from api.serializers import OrganizationSerializer
from organizations.models import Organization


class OrganizationCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
