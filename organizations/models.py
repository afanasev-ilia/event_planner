from django.db import models


class Organization(models.Model):
    title = models.CharField(
        'название',
        max_length=200,
        help_text='название организации',
    )
    description = models.TextField(
        'описание',
        help_text='описание организации',
    )
    address = models.CharField(
        'адрес',
        max_length=250,
        help_text='адрес организации',
    )
    postcode = models.CharField(
        'почтовый индекс',
        max_length=50,
        help_text='почтовый индекс организации',
    )

    class Meta:
        verbose_name = 'организация'
        verbose_name_plural = 'организации'

    def __str__(self) -> str:
        return self.title
