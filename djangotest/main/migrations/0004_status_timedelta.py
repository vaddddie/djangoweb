# Generated by Django 4.1.dev20220406104243 on 2022-04-25 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_status_macaddress_alter_status_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='TimeDelta',
            field=models.DateTimeField(default=132, verbose_name='TimePass:'),
            preserve_default=False,
        ),
    ]
