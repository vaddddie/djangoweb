# Generated by Django 4.1 on 2022-11-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cell_humidity_arrow_cell_temperature_arrow_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='Image',
            field=models.ImageField(default='/main/static/main/favicon.ico', upload_to='cells/%Y-%m-%d/', verbose_name='Cell image:'),
        ),
    ]
