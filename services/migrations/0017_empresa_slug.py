# Generated by Django 3.2.2 on 2022-08-13 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_auto_20220813_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
