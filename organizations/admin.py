from django.contrib import admin

from organizations.models import Organization


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
