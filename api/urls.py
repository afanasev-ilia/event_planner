from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import OrganizationCreateViewSet, EventCreateRetrieveListViewSet

router = DefaultRouter()
router.register(
    'events',
    EventCreateRetrieveListViewSet,
    basename='events',
)
router.register(
    'organizations',
    OrganizationCreateViewSet,
    basename='organizations',
)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('chat/', include('chat.urls')),
]
