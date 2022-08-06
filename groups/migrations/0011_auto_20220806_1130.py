# Generated by Django 3.2.2 on 2022-08-06 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0010_auto_20220805_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postulation',
            name='group',
        ),
        migrations.AddField(
            model_name='postulation',
            name='group',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='groups.group'),
            preserve_default=False,
        ),
    ]
