# Generated by Django 3.2.2 on 2022-08-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0012_alter_postulation_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulation',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
