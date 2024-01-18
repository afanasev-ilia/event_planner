from django.contrib import admin
from django.urls import include, path

from chat.apps import ChatConfig
from organizations.apps import OrganizationsConfig

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls', namespace=ChatConfig.name)),
    path(
        'organizations/',
        include('organizations.urls', namespace=OrganizationsConfig.name),
    ),
]
