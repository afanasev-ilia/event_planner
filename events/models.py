from django.db import models

from organizations.models import Organization


class Event(models.Model):
    title = models.CharField(
        'название',
        max_length=200,
        help_text='название организации',
    )
    description = models.TextField(
        'описание',
        help_text='описание организации',
    )
    organizations = models.ManyToManyField(
        Organization,
        help_text='выберите организации',
    )
    image = models.ImageField(
        'изображение',
        upload_to='events/',
        help_text='добавьте изображение',
    )
    date = models.DateField(
        help_text='выберите дату мероприятия',
    )

    class Meta:
        verbose_name = 'мероприятие'
        verbose_name_plural = 'мероприятия'

    def __str__(self) -> str:
        return self.title
