# Generated by Django 3.2.2 on 2022-08-13 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_alter_empresa_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='slug',
            field=models.CharField(max_length=10),
        ),
    ]
