from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'phone_number',
        'email',
        'first_name',
        'last_name',
        'password',
    )
    list_editable = (
        'username',
        'email',
        'first_name',
        'last_name',
        'password',
    )
    search_fields = (
        'username',
        'first_name',
        'last_name',
    )
    list_filter = (
        'username',
        'email',
    )
