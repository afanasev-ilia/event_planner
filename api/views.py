from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import OrganizationSerializer, EventSerializer
from organizations.models import Organization
from events.models import Event


class EventCreateRetrieveListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    filterset_fields = ('date',)
    search_fields = ('title',)
    ordering_fields = ('date',)
    pagination_class = LimitOffsetPagination


class OrganizationCreateViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
