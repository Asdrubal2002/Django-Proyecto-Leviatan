# Generated by Django 3.2.2 on 2022-08-12 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20220812_1830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='slug',
            new_name='nombre',
        ),
    ]
