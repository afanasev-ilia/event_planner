from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

from events.views import EventCreateRetrieveListViewSet
from organizations.views import OrganizationCreateViewSet

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
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


schema_view = get_schema_view(
   openapi.Info(
      title='Event_planner API',
      default_version='v1',
      description='Документация для проекта Event_planner',
      contact=openapi.Contact(email='iafansevmail@gmail.com'),
      license=openapi.License(name='MIT License'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$',
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'),
]
