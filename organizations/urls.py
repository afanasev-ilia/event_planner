from django.urls import path

from organizations import views
from organizations.apps import OrganizationsConfig

app_name = OrganizationsConfig.name

urlpatterns = [
    path('', views.OrganizationCreate.as_view()),
]
