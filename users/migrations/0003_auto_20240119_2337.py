# Generated by Django 3.2 on 2024-01-19 20:37

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20240119_2310'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
