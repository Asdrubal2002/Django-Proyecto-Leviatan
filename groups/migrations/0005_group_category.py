# Generated by Django 3.2.2 on 2022-08-03 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_group_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
