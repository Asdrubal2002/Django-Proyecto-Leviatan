# Generated by Django 3.2.2 on 2022-08-01 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='forma',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
