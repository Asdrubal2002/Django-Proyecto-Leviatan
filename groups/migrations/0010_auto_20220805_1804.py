# Generated by Django 3.2.2 on 2022-08-05 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0009_alter_group_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulation',
            name='hope',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='postulation',
            name='presentation',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='postulation',
            name='why',
            field=models.TextField(max_length=300),
        ),
    ]