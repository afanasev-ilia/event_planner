# Generated by Django 3.2 on 2024-01-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='название организации', max_length=200, verbose_name='название')),
                ('description', models.TextField(help_text='описание организации', verbose_name='описание')),
                ('address', models.CharField(help_text='адрес организации', max_length=250, verbose_name='адрес')),
                ('postcode', models.CharField(help_text='почтовый индекс организации', max_length=50, verbose_name='почтовый индекс')),
            ],
            options={
                'verbose_name': 'организация',
                'verbose_name_plural': 'организации',
            },
        ),
    ]
