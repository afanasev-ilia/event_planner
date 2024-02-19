from rest_framework import mixins, viewsets

from organizations.serializers import OrganizationSerializer
from organizations.models import Organization


class OrganizationCreateViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
