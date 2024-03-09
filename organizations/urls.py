from django.urls import include, path
from rest_framework.routers import DefaultRouter

from organizations.views import OrganizationCreateViewSet

router = DefaultRouter()
router.register(
    'organizations',
    OrganizationCreateViewSet,
    basename='organizations',
)

urlpatterns = [
    path('', include(router.urls)),
]
