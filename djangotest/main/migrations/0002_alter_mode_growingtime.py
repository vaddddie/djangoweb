# Generated by Django 4.0.4 on 2022-05-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mode',
            name='GrowingTime',
            field=models.DurationField(default='00:00:00', verbose_name='GrowingTime:'),
        ),
    ]