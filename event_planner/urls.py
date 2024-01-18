from django.contrib import admin
from django.urls import include, path

from chat.apps import ChatConfig


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls', namespace=ChatConfig.name)), # поменять адресс чата?
    path('api/v1/', include('api.urls'), name='api'),
]
