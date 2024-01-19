from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import OrganizationCreate

router = DefaultRouter()
router.register('organizations', OrganizationCreate, basename='organizations')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
