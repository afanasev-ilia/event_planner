from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import OrganizationCreate, EventCreate

router = DefaultRouter()
router.register('events', EventCreate, basename='events')
router.register('organizations', OrganizationCreate, basename='organizations')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
