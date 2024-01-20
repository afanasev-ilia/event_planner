from django.contrib import admin
from django.contrib.auth import get_user_model

from organizations.models import Organization

User = get_user_model()


class EmployeeInline(admin.StackedInline):
    model = User
    fields = ('email',)
    readonly_fields = ('email',)
    extra = 0


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'address',
        'postcode',
    )
    search_fields = ('title',)
    list_filter = ('title',)
    inlines = [EmployeeInline]
