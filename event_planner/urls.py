from django.contrib import admin
from django.urls import include, path

from chat.apps import ChatConfig


urlpatterns = [
    path('chat/', include('chat.urls', namespace=ChatConfig.name)),
    path('admin/', admin.site.urls),
]
