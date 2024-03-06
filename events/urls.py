from rest_framework.routers import DefaultRouter

from events.views import EventCreateRetrieveListViewSet

router = DefaultRouter()
router.register(
    'events',
    EventCreateRetrieveListViewSet,
    basename='events',
)
