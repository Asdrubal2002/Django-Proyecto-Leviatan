# Generated by Django 3.2.2 on 2022-08-03 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_group_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='miembros',
            new_name='numero_miembros',
        ),
    ]
