# Generated by Django 3.2.2 on 2022-07-31 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]
