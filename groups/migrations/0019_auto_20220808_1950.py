# Generated by Django 3.2.2 on 2022-08-09 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0018_rename_postulant_postulation_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postulation',
            name='hope',
        ),
        migrations.RemoveField(
            model_name='postulation',
            name='why',
        ),
        migrations.AlterField(
            model_name='postulation',
            name='presentation',
            field=models.TextField(max_length=400),
        ),
    ]