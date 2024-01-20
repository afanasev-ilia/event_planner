from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'email',
        'phone_number',
        'first_name',
        'last_name',
        'password',
        'organization',
    )
    list_editable = (
        'email',
        'phone_number',
        'first_name',
        'last_name',
        'password',
    )
    search_fields = (
        'email',
    )
    list_filter = (
        'first_name',
        'last_name',
    )
