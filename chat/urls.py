from django.urls import path

from chat import views
from chat.apps import ChatConfig

app_name = ChatConfig.name

urlpatterns = [
    path('', views.index, name='index'),
]
