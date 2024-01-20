from django.contrib import admin
from django.utils.safestring import mark_safe

from events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'get_image',
        'date',
    )
    filter_horizontal = ('organizations',)
    search_fields = ('title',)
    list_filter = ('title',)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"
