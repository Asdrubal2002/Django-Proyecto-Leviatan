# Generated by Django 3.2.2 on 2022-08-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_alter_work_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
