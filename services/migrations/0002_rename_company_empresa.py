# Generated by Django 3.2.2 on 2022-08-12 22:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Company',
            new_name='Empresa',
        ),
    ]
