# Generated by Django 4.1.dev20220406104243 on 2022-04-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_status_growthprocess_status_timeleft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='TimeLeft',
            field=models.DateTimeField(verbose_name='Time Left:'),
        ),
    ]
