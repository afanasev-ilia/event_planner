from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from chat.apps import ChatConfig


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls', namespace=ChatConfig.name)),  # поменять адресс чата?
    path('api/v1/', include('api.urls'), name='api'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
