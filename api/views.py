import asyncio
import time
from asgiref.sync import sync_to_async, async_to_sync
from rest_framework import mixins, viewsets, filters, status
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import OrganizationSerializer, EventSerializer
from organizations.models import Organization
from events.models import Event


# class EventCreateRetrieveListViewSet(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     viewsets.GenericViewSet,
# ):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter,
#                        filters.OrderingFilter)
#     filterset_fields = ('date',)
#     search_fields = ('title',)
#     ordering_fields = ('date',)
#     pagination_class = LimitOffsetPagination

#     async def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         await sync_to_async(serializer.is_valid(raise_exception=True))
#         await self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         await asyncio.sleep(60)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#     @sync_to_async
#     def perform_create(self, serializer):
#         serializer.save()


class OrganizationCreateViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
